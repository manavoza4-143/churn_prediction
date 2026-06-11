from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load(r"I:\amzon-project\churn_predicion\model.pkl")

@app.route("/")
def home():
    return "Churn Prediction API (Production Ready)"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Incoming:", data)

        input_df = pd.DataFrame([data])
        print("DataFrame:", input_df)

        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        return jsonify({
            "churn": int(prediction),
            "probability": float(prob)
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)

print(model.feature_names_in_)