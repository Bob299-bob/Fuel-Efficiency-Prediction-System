# 🚗 Fuel Efficiency Prediction System

An end-to-end Machine Learning project that predicts a vehicle’s fuel efficiency (Miles Per Gallon - MPG) based on engine and performance features using a TensorFlow regression model.

---

## 🌐 Live Demo
👉 https://ai-fuel-effi-jabjgbwaznscfb5refetki.streamlit.app/

---

## 📌 Project Overview
This project uses a deep learning regression model to predict fuel efficiency of vehicles. The system takes input features like engine size, horsepower, weight, acceleration, and model year to estimate MPG.

---

## ⚙️ Features
- 🚀 Regression-based ML model (TensorFlow)
- 📊 Real-time MPG prediction
- 🧹 Data preprocessing & cleaning
- 📉 Actual vs Predicted visualization
- 🌐 Interactive Streamlit web app
- 📦 End-to-end ML pipeline

---

## 🧠 Problem Faced & Solution

### ⚠️ Problem:
- Missing values were represented as “?”
- Mixed data types (string + numeric)
- Errors during `fillna(data.mean())`
- Data not suitable for ML training

### 🔧 Solution:
- Replaced “?” with NaN
- Converted columns to numeric (float)
- Applied mean imputation
- Cleaned dataset for model training

---

## 🛠 Tech Stack
- Python  
- TensorFlow  
- Scikit-learn  
- Pandas  
- NumPy  
- Matplotlib  
- Joblib  
- Streamlit  

---

## 📊 Model Type
✔ Regression Model (Deep Learning using TensorFlow)  
✔ Output: Continuous value (MPG)

---


streamlit run app.py
