from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    return 'Hello, World!'


@app.get('/about')
def about():
    return 'About'
