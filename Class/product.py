from google.cloud import language
from google.oauth2 import service_account
import pandas as pd
import numpy as np
import time
from pandas_profiling import ProfileReport

start = time.time() # start the timer

def analyze_text_sentiment(text):
    # load the key file
    creds = service_account.Credentials.from_service_account_file('noble-catcher-405216-f75b4eac970d.json')
    # convert the text into a document type
    client = language.LanguageServiceClient(credentials=creds, )
    docinput = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    # call function to analysis the sentiment of the text
    response = client.analyze_sentiment(document= docinput)
    # get the results in variable sentiment
    sentiment = response.document_sentiment
    #print the sentiment score
    return (sentiment.score,sentiment.magnitude)

    # call function to analysis the sentiment of the text


counter = 0

df = pd.read_csv('productreviews.csv')
profile = ProfileReport(df)
df=pd.DataFrame(df)
print(df.head(10))
df=df[df['Review'].notna()]
df=df.reset_index()
df=df.drop(columns='index')
df=df[0:5000]
test=analyze_text_sentiment(df['Review'].iloc[0])
print('The sentiment score is',test[0])
print('The magnitude of sentiment score is',test[1])
df['Score']=np.NaN
df['Magnitude']=np.NaN
for index, row in df.iterrows():
    text = df.at[index,'Review']
    df.at[index,'Score']=analyze_text_sentiment(text)[0]
    df.at[index,'Magnitude']=analyze_text_sentiment(text)[1]
    counter += 1
    if counter % 500 == 0:  # check if the counter is divisible by 500
        time.sleep(90)
end = time.time()
df.to_csv('productreviewssentiment.csv')
print(df.dtypes)
