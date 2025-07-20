# Credit-card-Default-Prediction-using-Machine-learning
A machine learning-based web application built with Flask to predict credit card default risk. It uses Logistic Regression on a preprocessed dataset and provides a user-friendly interface to input data and receive predictions.

## 📌 Objective
To predict credit card default using machine learning techniques and provide an interactive web application for end users.

## 🧰 Libraries Used

- **Flask**: For building the web application.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For model building and training.
- **Joblib**: For saving and loading the trained model.
- **HTML/CSS**: For designing the front-end interface.

## 🛠️ Requirements

Make sure the following are installed:

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Joblib

Install the dependencies using:
pip install -r requirements.txt

**Project Workflow**
1. Data Preparation:
- Collected the credit card default dataset (client.csv)
- Cleaned and preprocessed the data
- Split the dataset into features (X) and target variable (y)

2. Model Training:
- Used Logistic Regression algorithm for classification
- Trained the model on the preprocessed data
- Saved the trained model and scaler using joblib

3. Web Application Development:
- Created a Flask web application (app.py)
- Designed index.html for input and result.html for output
- Styled the pages with styles.css

4. Integration
- Integrated the trained model into the Flask app
- Defined routes to render the input form and display predictions
