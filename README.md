# 🧠 MNIST Digit Classifier API (FastAPI)

A simple machine learning project that demonstrates how to train, serve, and deploy a handwritten digit classifier using **TensorFlow** and **FastAPI**.

This project exposes:

- a **public JSON API** for predictions
- a **lightweight HTML demo UI** for manual testing

The model is trained on the **MNIST dataset** and is intended for **educational and demo purposes**.

---

## ✨ Features

- ✅ Trained on MNIST handwritten digits (0–9)
- ✅ Public API endpoint returning JSON
- ✅ Simple web interface for human testing
- ✅ Minimal preprocessing for API stability
- ✅ Easy to deploy (Railway / Render / VPS)

---

## 📂 Project Structure

```text
ai-mnist/
├── app.py          # FastAPI application
├── model.h5        # Trained MNIST model
├── samples/        # Sample MNIST images (0–9)
│   ├── sample_0.png
│   ├── sample_1.png
│   └── ...
├── make_samples.py # Script to generate MNIST samples
└── README.md
```

---

## 🧠 Model Scope & Limitations

This model is **optimized for MNIST-style inputs only**.

Best results are achieved when:

- the image contains **a single handwritten digit**
- the digit is **clearly visible and centered**
- the image is **28×28 pixels**
- the image is **grayscale** (MNIST format)

⚠️ Predictions for non-MNIST-style images (photos, colored images, complex backgrounds) are **not guaranteed**.

---

## 🚀 Getting Started (Local)

### 1️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install fastapi uvicorn tensorflow pillow
```

### 3️⃣ Run the server

```bash
uvicorn app:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000
```

---

## 🌐 Web Demo (HTML)

The root endpoint provides a simple web UI:

```http
GET /
```

Features:

- Upload an image
- See predicted digit and confidence
- Download and test with MNIST sample images

This UI is intended for **manual testing and demonstration**.

---

## 🔌 Public API (JSON)

### Endpoint

```http
POST /api/predict
```

### Request

- Content-Type: `multipart/form-data`
- Body:

  - `file`: image file (PNG/JPG)

Example using `curl`:

```bash
curl -X POST http://127.0.0.1:8000/api/predict \
  -F "file=@samples/sample_2.png"
```

### Response

```json
{
  "digit": 2,
  "confidence": 0.9995
}
```

---

## 🧪 Sample Images

Sample MNIST images are available in the `/samples` directory and can be downloaded directly from the web UI.

You can regenerate them using:

```bash
python make_samples.py
```

---

## 🏗 Deployment

This project can be deployed easily to:

- Railway
- Render
- any VPS with Python support

### Start command

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

## 📚 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **FastAPI**
- **Pillow (PIL)**
- **Uvicorn**

---

## 🎯 Project Goal

This project is designed as:

- a learning exercise for ML deployment
- a simple example of ML inference as an API
- a portfolio-friendly demonstration of an end-to-end ML workflow

It does **not** aim to be a production-grade OCR system.

---

## 📄 License

This project is released for educational purposes.
