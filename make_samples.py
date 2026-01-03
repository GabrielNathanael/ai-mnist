import tensorflow as tf
from PIL import Image
import os

(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
os.makedirs("samples", exist_ok=True)

picked = set()
for img, label in zip(x_test, y_test):
    if label not in picked:
        Image.fromarray(img).save(f"samples/sample_{label}.png")
        picked.add(label)
    if len(picked) == 10:
        break

print("MNIST samples saved in ./samples")
