from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse,HTMLResponse
import pickle
import pandas as pd
import numpy as np
from fastapi.templating import Jinja2Templates


from logging_config import get_logger

logger = get_logger(__name__)

app = FastAPI()

# Load your model
model_path = "models/pipeline.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

class ModelInput(BaseModel):
    cap_diameter: float = Field(..., alias='cap-diameter')
    cap_shape: str = Field(..., alias='cap-shape')
    cap_surface: str = Field(..., alias='cap-surface')
    cap_color: str = Field(..., alias='cap-color')
    does_bruise_or_bleed: str = Field(..., alias='does-bruise-or-bleed')
    gill_attachment: str = Field(..., alias='gill-attachment')
    gill_spacing: str = Field(..., alias='gill-spacing')
    gill_color: str = Field(..., alias='gill-color')
    stem_height: float = Field(..., alias='stem-height')
    stem_width: float = Field(..., alias='stem-width')
    stem_root: str = Field(..., alias='stem-root')
    stem_surface: str = Field(..., alias='stem-surface')
    stem_color: str = Field(..., alias='stem-color')
    veil_type: str = Field(..., alias='veil-type')
    veil_color: str = Field(..., alias='veil-color')
    has_ring: str = Field(..., alias='has-ring')
    ring_type: str = Field(..., alias='ring-type')
    spore_print_color: str = Field(..., alias='spore-print-color')
    habitat: str
    season: str = Field(..., alias='season')

    class Config:
        allow_population_by_field_name = True

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return HTMLResponse(content="<h1>Welcome to the Mushroom Prediction API!</h1><p>Use the /predict endpoint to make predictions.</p>")
    
@app.post("/predict")
async def predict(input_data: ModelInput):
    try:
        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data.model_dump(by_alias=True)])  # Use dict() instead of model_dump()
        # Print for debugging
        print("Input DataFrame shape:", input_df.shape)  
        print("Input DataFrame columns:", input_df.columns.tolist())  
        print("Input DataFrame:", input_df)
        prediction = model.predict(input_df)

        # Get the prediction
        prediction_value = prediction[0].item() if isinstance(prediction[0], (np.integer, np.floating)) else prediction[0]
        cg = 'Poisonous' if prediction_value == 1 else 'Edible'
        # Return the prediction
        return JSONResponse(content={"prediction": cg})  # Assuming prediction is an array
    except Exception as e:
        print("An error occurred:", e)
        raise HTTPException(status_code=500, detail=str(e))
