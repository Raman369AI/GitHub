from fastapi import FastAPI
app = FastAPI()

Books=[{'title':'Raman','author':'Raman','category':'raman'},
       {'title':'Raman','author':'Raman','category':'raman'},
       {'title':'Raman','author':'Raman','category':'raman'},
       {'title':'Raman','author':'Raman','category':'raman'},
       {'title':'Raman','author':'Raman','category':'raman'}]
#http request to get the data
@app.get("/books")
async def first_api():
    return Books
