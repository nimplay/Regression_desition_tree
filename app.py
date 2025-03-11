import streamlit as st
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the application
st.title("House Price Forecast 🏠")

# Path to CSV file and model
DEFAULT_DATA_FILE = 'house_prices.csv'
MODEL_FILE = 'decision_tree_model.pkl'

# Function to train and save the model
def train_and_save_model(data):
    # Divide the data into characteristics (X) and target (y)
    X = data[['Size', 'Bedrooms']]
    y = data['Price']

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creating and training the model
    regressor = DecisionTreeRegressor(random_state=42)
    regressor.fit(X_train, y_train)

    # Saving the model to a file
    joblib.dump(regressor, MODEL_FILE)
    st.success("Model trained and stored in 'decision_tree_model.pkl'")

# Load the model (if any)
if os.path.exists(MODEL_FILE):
    regressor = joblib.load(MODEL_FILE)
    st.success("Model loaded from 'decision_tree_model.pkl'")
else:
    st.info("No trained model was found. Please upload a CSV file to train the model.")

# Interface for uploading a CSV file
st.sidebar.header("Upload File CSV")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Upload data from the uploaded file or use default data
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.sidebar.success("CSV file successfully uploaded.")
else:
    st.sidebar.info("Using default data.")
    data = pd.read_csv(DEFAULT_DATA_FILE)

# Show uploaded data
st.header("Data Uploaded")
st.write(data)

# Graphical display
st.header("Data Visualisation")

# Graph 1: Price distribution
st.subheader("Price Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(data['Price'], kde=True, ax=ax1)
st.pyplot(fig1)

# Figure 2: Relationship between size and price
st.subheader("Relationship between size and price")
fig2, ax2 = plt.subplots()
sns.scatterplot(x=data['Size'], y=data['Price'], ax=ax2)
st.pyplot(fig2)

# Figure 3: Ratio of rooms to price
st.subheader("Relationship between rooms and price")
fig3, ax3 = plt.subplots()
sns.boxplot(x=data['Bedrooms'], y=data['Price'], ax=ax3)
st.pyplot(fig3)

# Train the model if a new CSV file is uploaded
if uploaded_file is not None:
    if st.sidebar.button("Train Model with New Data"):
        train_and_save_model(data)
        regressor = joblib.load(MODEL_FILE)

# User interface for making predictions
st.header("Enter the details of the house")

# Inputs del usuario
size = st.number_input("Size (square feet):", min_value=500, max_value=3000, value=1500)
bedrooms = st.number_input("Number of rooms:", min_value=1, max_value=6, value=3)

# Button to make the prediction
if st.button("Predict Price"):
    # Making the prediction
    input_data = pd.DataFrame([[size, bedrooms]], columns=['Size', 'Bedrooms'])
    predicted_price = regressor.predict(input_data)[0]

    # Show the result
    st.success(f"The predicted price of the house is: **${predicted_price:,.2f}**")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 16px;
    }
    </style>
    <div class="footer">
        <p>© 2025 Nimrod Acosta</p>
    </div>
    """,
    unsafe_allow_html=True
)
