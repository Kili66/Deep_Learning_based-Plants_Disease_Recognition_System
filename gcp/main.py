import tensorflow as tf
import numpy as np
from google.cloud import storage
from PIL import Image

BUCKET_NAME = "trained-model-bucket"

CLASS_NAMES = ["Apple Black Rot", "Apple Healthy", "Apple Scab", "Apple Cedar Rust"]

model = None

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    
    
def predict_keras(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/apple.h5",
            "/tmp/apple.h5",
        )
        model = tf.keras.models.load_model("/tmp/apple.h5")
        
    image = request.files["file"]
    image = np.array(Image.open(image).convert("RGB").resize((256,256)))
    image = image/255
    img_array = tf.expand_dims(image, 0)
    
    predictions = model.predict(img_array)
    print(predictions)
    
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    
    return {
        "class": predicted_class,
        "confidence": confidence
    }
