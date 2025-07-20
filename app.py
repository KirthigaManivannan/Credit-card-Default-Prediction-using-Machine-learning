from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('credit_default_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data from form
        form_data = request.form.to_dict()
        
        # Convert 'SEX' value to integer
        form_data['SEX'] = int(form_data['SEX'])
        
        # Create DataFrame from form data
        data = pd.DataFrame(form_data, index=[0])
        
        # Prediction
        prediction = model.predict(data)[0]
        
        result = 'Default' if prediction == 1 else 'Not Default'
        
        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
