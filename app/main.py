from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GeoQuiz API is running"}