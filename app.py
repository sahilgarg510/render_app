from flask import Flask, request , jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Ml model is live"

@app.route('/predict' , methods=['POST'])
def predict():
    try:
        data = request.get_json(force = True)
        features = np.array(data['features']).reshape(1,-1)
        prediction = model.predict(features)
        value = "legitimate"
        if int(prediction[0]) == 1:
            value = "Phishing"
        return jsonify({'prediction':value})
    
    except Exception as e:
        return jsonify({'error':str(e)})
    
if __name__ == '__main__':
    app.run(debug = True)