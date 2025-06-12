from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline.stage4_model_eval import ModelEvalutionPipeline
import os
import uvicorn

app = FastAPI()

class RequestText(BaseModel):
    text: str

@app.get("/train")
async def training():
    try:
        os.system("python3 main.py")
        return {"message": "Training Finished"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predict")
async def predict(text):
    try:
        pred_pipe = ModelEvalutionPipeline()
        result = pred_pipe.intiate_model_eval(text)
        return {"prediction": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
