import requests
import tensorflow as tf

# Ambil 1 sample MNIST
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

sample = x_test[0]           # shape (28, 28)
label = y_test[0]

pixels = sample.flatten().tolist()

res = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"pixels": pixels}
)

print("True label:", label)
print("API response:", res.json())
