from fastapi import FastAPI, UploadFile, File
from app import load_excel, analyze_data
from llm import generate_response

app = FastAPI()

@app.post("/upload/")
async def upload_excel(file: UploadFile = File(...)):
    df = load_excel(file.file)
    analysis = analyze_data(df)
    return {"analysis": analysis}

@app.post("/generate/")
async def generate(prompt: str):
    response = generate_response(prompt)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
