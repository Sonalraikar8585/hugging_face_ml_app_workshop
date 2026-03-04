# 🏠 House Price Prediction App

🔗 **Live Demo:** https://huggingface.co/spaces/Sonal85/hf_ml_app  

A simple Machine Learning web application that predicts house prices based on:

- 📏 Area (in square feet)
- 🛏 Number of Bedrooms

The model is built using **Linear Regression (Scikit-learn)** and deployed using **Gradio** on Hugging Face Spaces.

---

## 🚀 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Gradio
- Hugging Face Spaces

---

## 📂 Project Structure
hf_ml_app/
│
├── app.py # Gradio application
├── model.pkl # Trained ML model
├── requirements.txt
└── README.md


---

## 🧠 Model Details

The model is trained using **Linear Regression** on a small sample dataset.

### Training Dataset

| Area (sq ft) | Bedrooms | Price |
|-------------|----------|--------|
| 1000        | 2        | 50     |
| 1500        | 3        | 75     |
| 2000        | 3        | 100    |
| 2500        | 4        | 130    |
| 3000        | 4        | 150    |

- **Features:** area, bedrooms  
- **Target:** price  

---

## ⚙️ How It Works

1. User enters:
   - Area
   - Number of Bedrooms  
2. Input is converted into a NumPy array.
3. The trained model predicts the house price.
4. The predicted result is displayed instantly.

---

## 🛠 Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://huggingface.co/spaces/Sonal85/hf_ml_app
cd hf_ml_app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
python app.py

📦 requirements.txt
pandas
numpy
scikit-learn
gradio

🌐 Deployment

This project is deployed using Gradio on Hugging Face Spaces.

Live App:
https://huggingface.co/spaces/Sonal85/hf_ml_app

🎯 Future Improvements

Train model on real-world housing dataset

Add model evaluation metrics (R², MAE, etc.)

Improve UI with sliders and styling

Add input validation

Deploy using Docker

👩‍💻 Author

Sonal Raikar
GitHub: https://github.com/Sonalraikar8585

LinkedIn: https://www.linkedin.com/in/sonal-raikar
