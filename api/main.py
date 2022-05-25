from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# We'll use an endpoint instead of the model written below 
MODEL_APPLE = tf.keras.models.load_model("C:/Users/q/Downloads/All_Data/saved_models/1")
CLASS_NAMES_APPLE = ["Apple Black Rot", "Apple Healthy", "Apple Scab", "Apple Cedar Rust"]

MODEL_TOMATO = tf.keras.models.load_model("C:/Users/q/Downloads/All_Data/saved_models/5")
CLASS_NAMES_TOMATO = ["Tomato Bacterial Spot", "Tomato Early Blight", "Tomato Healthy", "Tomato Late Blight"]

MODEL_GRAPE = tf.keras.models.load_model("C:/Users/q/Downloads/All_Data/saved_models/3")
CLASS_NAMES_GRAPE = ["Grape Black Measles", "Grape Black Rot", "Grape Healthy", "Grape Isariopsis Leaf Spot"]

MODEL_CORN = tf.keras.models.load_model("C:/Users/q/Downloads/All_Data/saved_models/2")
CLASS_NAMES_CORN = ["Corn Common rust", "Corn Gray leaf spot", "Corn Healthy", "Corn Northern Leaf Blight"]

MODEL_POTATO = tf.keras.models.load_model("C:/Users/q/Downloads/All_Data/saved_models/4")
CLASS_NAMES_POTATO = ["Potato Early Blight", "Potato Healthy", "Potato Infestans", "Potato Late Blight"]

@app.get("/ping")
async def ping():
    return "Hello, I'm alive bruhh let's go now! come with me"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/prediction_apple")
async def prediction(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    data = MODEL_APPLE.predict(img_batch)
    predicted_class = CLASS_NAMES_APPLE[np.argmax(data[0])]
    confidence = np.max(data[0]) # This is the acuuracy's percentage
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/prediction_potato")
async def prediction(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    data = MODEL_POTATO.predict(img_batch)
    predicted_class = CLASS_NAMES_POTATO[np.argmax(data[0])]
    confidence = np.max(data[0]) # This is the acuuracy's percentage
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/prediction_tomato")
async def prediction(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    data = MODEL_TOMATO.predict(img_batch)
    predicted_class = CLASS_NAMES_TOMATO[np.argmax(data[0])]
    confidence = np.max(data[0]) # This is the acuuracy's percentage
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/prediction_corn")
async def prediction(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    data = MODEL_CORN.predict(img_batch)
    predicted_class = CLASS_NAMES_CORN[np.argmax(data[0])]
    confidence = np.max(data[0]) # This is the acuuracy's percentage
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
    
@app.post("/prediction_grape")
async def prediction(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    data = MODEL_GRAPE.predict(img_batch)
    predicted_class = CLASS_NAMES_GRAPE[np.argmax(data[0])]
    confidence = np.max(data[0]) # This is the acuuracy's percentage
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }



if __name__ == "__main__":
    # uvicorn.run(app, host="localhost", port=8080)
    uvicorn.run("main:app", host="localhost", port=8080)
    # i shouldn't use reload in production on windows...