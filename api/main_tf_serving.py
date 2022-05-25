from aiohttp import request
from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image  # from pillow module
import tensorflow as tf
import requests # This module is used to make the http call for the prediction

app = FastAPI()

# We'll use an endpoint instead of the model written below 
endpoint = "http://localhost:8501/v1/models/Apple_model:predict"
MODEL = tf.keras.models.load_model("C:/Users/q/Downloads/All_Data/saved_models/1")
CLASS_NAMES = ["Apple Black Rot", "Apple Healthy", "Apple Scab", "Cedar Apple Rust"]


@app.get("/ping_serving")
async def ping():
    return "Sniper out now..."


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(img_batch)

    json_data = {
        "instances": img_batch.tolist()
        # We converted to list bcz this is the format expected by the json file
    }
    response = requests.post(endpoint, json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    return {
        "Class": predicted_class,
        "Confidence": float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run("main_tf_serving:app", host="127.0.0.1", port=8080)
    # we shouldn't use reload in production on windows...
