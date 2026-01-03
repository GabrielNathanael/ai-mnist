import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# load model once
model = tf.keras.models.load_model("model.h5")

def predict(img: Image.Image):
    # convert to grayscale
    img = img.convert("L")

    # simple MNIST-style preprocessing
    img = img.resize((28, 28))

    x = np.array(img).astype("float32") / 255.0
    x = x.reshape(1, 28, 28)

    preds = model.predict(x)
    digit = int(np.argmax(preds))
    confidence = float(np.max(preds))

    return {
        "Digit": digit,
        "Confidence": round(confidence, 4)
    }

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload a digit image"),
    outputs=gr.JSON(label="Prediction"),
    title="MNIST Digit Classifier",
    description=(
        "A simple demo of a handwritten digit classifier trained on the MNIST dataset.\n\n"
        "Best results are achieved with MNIST-style images: "
        "single digit, centered, grayscale, 28×28."
    ),
    examples=[
        "samples/sample_0.png",
        "samples/sample_1.png",
        "samples/sample_2.png",
        "samples/sample_3.png",
        "samples/sample_4.png",
        "samples/sample_5.png",
        "samples/sample_6.png",
        "samples/sample_7.png",
        "samples/sample_8.png",
        "samples/sample_9.png",
    ],
)

demo.launch()
