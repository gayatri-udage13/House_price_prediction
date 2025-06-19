from flask import Flask, render_template, request
import pickle
import numpy as np

# ✅ Create the Flask app before any routes
app = Flask(__name__)

# ✅ Load the trained model
with open('house_price_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

# ✅ Home route
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[field]) for field in [
            'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
            'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']]
        features_array = np.array([features])
        prediction = model.predict(features_array)
        output = round(prediction[0] * 1000, 2)

        if output < 150000:
            price_class = "low"
        elif output <= 300000:
            price_class = "medium"
        else:
            price_class = "high"

        return render_template(
            'index.html',
            prediction_text=f"Predicted Price: ₹{output:,.2f}",
            price_class=price_class,
            predicted_price=output  # For graph display
        )

    except Exception as e:
        return f"❌ Error: {str(e)}"

# ✅ Insights route
@app.route('/insights')
def insights():
    return render_template('insights.html')

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)
