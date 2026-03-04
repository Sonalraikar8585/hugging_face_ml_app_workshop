import gradio as gr
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(area, bedrooms):
    data = np.array([[area, bedrooms]])
    prediction = model.predict(data)
    return float(prediction[0])

interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Area (sq ft)"),
        gr.Number(label="Number of Bedrooms")
    ],
    outputs="number",
    title="House Price Prediction",
    description="Enter area and bedrooms to predict price"
)

interface.launch()
