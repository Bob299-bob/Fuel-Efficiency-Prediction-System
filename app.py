import streamlit as st
import tensorflow as tf
import joblib
model=tf.keras.models.load_model('fuel_efficiency.h5')
scaler=joblib.load('scaler.pkl')
if "page" not in st.session_state:
    st.session_state.page = "Home"
# Sidebar
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("📊 Visualization"):
    st.session_state.page = "Visualization"
if st.session_state.page == "Home":
    st.title("🚗 Fuel Efficiency Prediction System")
    st.markdown("""
    Predict a vehicle's fuel efficiency (**Miles Per Gallon - MPG**) using a trained TensorFlow Machine Learning model.
    Enter the vehicle specifications below and click **Predict MPG** to estimate fuel efficiency.
    """)
    st.subheader("Vehicle Specifications")
    st.write("Provide the technical details of the vehicle:")
    data=["Cylinders","Displacement","Horsepower","Weight","Acceleration","Model_Year"]
    values=[]
    for  i in data:
        i=st.number_input(f"Enter{i}",min_value=0)
        values.append(i)
    origin=st.selectbox('Country of Origin 1:USA 2:Brazil 3:Canada',[1,2,3])
    values.append(origin)
    print([values])
    if(st.button('Predict')):
        scale_data=scaler.transform([values])
        prediction=model.predict(scale_data)
        st.success(f"Best MPG is:{prediction[0][0]:.2f}")
        st.balloons()
elif st.session_state.page == "Visualization":
    st.title("📊 Actual vs Predicted Visualization")
    import matplotlib.pyplot as plt
    pred=joblib.load('predict.pkl')
    actual=joblib.load('actual.pkl')
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(actual, pred)
    ax.set_xlabel("Actual MPG")
    ax.set_ylabel("Predicted MPG")
    ax.set_title("Actual vs Predicted Fuel Efficiency")
    st.pyplot(fig)
st.sidebar.title("🚗 Fuel Efficiency Predictor")

st.sidebar.markdown("""
### About
This application predicts vehicle fuel efficiency (MPG) using a trained TensorFlow regression model.

### Features
- TensorFlow Neural Network
- StandardScaler Preprocessing
- Real-time MPG Prediction
- Interactive Streamlit Interface

### Inputs
- Cylinders
- Displacement
- Horsepower
- Weight
- Acceleration
- Model Year
- Origin
""")
st.markdown("""
            <style>
                .stApp{
                    background-color:#0F172A;   
                }
               </style>
            """,unsafe_allow_html=True
            )
st.sidebar.markdown("""
            <style>
                .stApp{
                    background-color:#1E293B;   
                }
               </style>
            """,unsafe_allow_html=True
            )