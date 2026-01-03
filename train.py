import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load dataset MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Preprocess
# Normalize 
x_train = x_train / 255.0
x_test = x_test / 255.0

# 3. Build model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),   # 28x28 -> 784
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax") 
])

# 4. Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# 5. Train
model.fit(
    x_train,
    y_train,
    epochs=3,
    validation_split=0.1
)

# 6. Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# 7. Save model
model.save("model.h5")
print("Model saved as model.h5")
