# House Price Prediction with Decision Tree Regression

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

This project is an interactive web application built with Streamlit that uses a Decision Tree Regression model to predict house prices based on the size (in square feet) and the number of bedrooms. Additionally, it allows users to upload a custom CSV file to train the model and visualize data insights through interactive charts.

## Key Features
- Price Prediction: Enter the size of the house and the number of bedrooms to get a price prediction.

- Data Upload: Upload your own CSV file to train the model with new data.

- Data Visualization: Explore interactive charts to understand data distribution and relationships between features.

- Easy Deployment: The app can be deployed on Streamlit Sharing with just a few clicks.

## Requirements
To run this project, you need:

- Python 3.8 or higher.
- Libraries specified in requirements.txt.

## Installation

### Clone this repository:

git clone https://github.com/nimplay/Regression_desition_tree.git
cd house-price-prediction

### Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

### Install the dependencies:

pip install -r requirements.txt

## Running Locally

### Activate the virtual environment (if you created one):

source venv/bin/activate  # On Windows: .\venv\Scripts\activate

### Run the app:

streamlit run app.py

### Open your browser and go to http://localhost:8501.

## How to Use the App

### Upload Data:

- In the sidebar, upload a CSV file with columns Size, Bedrooms, and Price.
- If no file is uploaded, the app will use a default dataset.

### Visualize Data:

Explore the automatically generated charts:

  - Price Distribution: A histogram showing the distribution of house prices.
  - Size vs. Price: A scatter plot showing how house size affects price.
  - Bedrooms vs. Price: A box plot showing how the number of bedrooms affects price.

Train the Model:

  - If you uploaded a CSV file, click "Train Model with New Data" to update the model.

Predict Prices:

  - Enter the size of the house and the number of bedrooms.
  - Click "Predict Price" to get the prediction.

## Deploying to Streamlit Sharing

1- Upload the project to a GitHub repository.
2- Go to Streamlit Sharing and sign up with your GitHub account.
3- Click "New App" and fill in the details:

   - Select the repository and branch.
   - Specify the main file (app.py).

4- Click "Deploy". Streamlit will handle the rest.

5- Once deployed, the app will be available at a public link.

## Project Structure
/house-price-prediction/
│
├── app.py                # Main Streamlit application file
├── house_prices.csv      # Default training data CSV file
├── decision_tree_model.pkl # Trained model file
├── requirements.txt      # Dependencies file
└── README.md             # This file


## Dependencies
The project dependencies are listed in requirements.txt. You can install them with:
pip install -r requirements.txt

## Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

# Contact
If you have any questions or feedback, feel free to reach out:

Name: Nimrod Acosta

Email: [nimrod7day@gimail.com]

GitHub: [nimplay](https://github.com/nimplay)

Linkedin: [nimrod-acosta](https://www.linkedin.com/in/nimrod-acosta/)

Thanks for using this app! 🚀


