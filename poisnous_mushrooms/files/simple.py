import pandas as pd
import numpy as np
import lightgbm as lgb
import onnxmltools
import onnxruntime as rt
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.preprocessing import TargetEncoder
from sklearn.model_selection import train_test_split
from onnxmltools.convert.common.data_types import FloatTensorType

# Load and preprocess data
mushrooms = pd.read_csv("C://Users//raman//Downloads//train.csv", encoding_errors='ignore')
mushrooms['cap-diameter'] = mushrooms['cap-diameter'].astype(float)

# Process categorical columns
i_list = {}
for i in mushrooms.columns:
    if mushrooms[i].dtype == object:
        i_list[i] = mushrooms[i].value_counts().to_dict()
filtered_i_list = {col: {value: count for value, count in counts.items() if count >= 10} for col, counts in i_list.items()}
for i in filtered_i_list:
    mushrooms[i] = mushrooms[i].apply(lambda x: x if x in filtered_i_list[i].keys() else np.nan)
mushrooms['cap-diameter'].fillna(0, inplace=True)
mushrooms.fillna('Missing', inplace=True)

# Convert class to binary
Y_train = mushrooms['class'].apply(lambda x: 1 if x == 'p' else 0)
X_train = mushrooms.iloc[:, 2:]

# Encode categorical variables using TargetEncoder
enc_auto = TargetEncoder(smooth="auto")
X_trans = enc_auto.fit_transform(X_train, Y_train)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_trans, Y_train, test_size=0.3, random_state=42)

# Train LightGBM model
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)
params = {
    'objective': 'binary',
    'metric': 'binary_logloss',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}
lgb_model = lgb.train(
    params,
    train_data,
    num_boost_round=100,
    valid_sets=[train_data, test_data],
)

initial_types = [('input', FloatTensorType([None, X_train.shape[1]]))]

# Convert the LightGBM model to ONNX format
onnx_model = onnxmltools.convert_lightgbm(lgb_model, initial_types=initial_types)
onnxmltools.utils.save_model(onnx_model, 'lightgbm_mushrooms.onnx')

print("Model successfully converted to ONNX format and saved as 'lightgbm_mushrooms.onnx'.")

# Load the ONNX model and run inference
sess = rt.InferenceSession('lightgbm_mushrooms.onnx')
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

# Ensure the input data has the correct shape
# Convert X_test to the appropriate type
X_test = X_test.astype(np.float32)

# Perform inference on the test dataset
predictions = sess.run([output_name], {input_name: X_test})[0]

# Convert predictions to class labels (for binary classification)
predicted_labels = [1 if x > 0.5 else 0 for x in predictions]

# Calculate and print the accuracy of the ONNX model
accuracy_onnx = np.mean(predicted_labels == y_test)
print(f"Accuracy of the ONNX model: {accuracy_onnx:.2f}")