from flask import Flask, request, jsonify # type: ignore
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Salary Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        if "salary" not in data:
            return jsonify({
                "error": "salary field is required"
            }), 400

        salary = data["salary"]

        if not isinstance(salary, (int, float)):
            return jsonify({
                "error": "salary must be a number"
            }), 400

        if salary < 0:
            return jsonify({
                "error": "salary cannot be negative"
            }), 400

        prediction = model.predict([[salary]])

        return jsonify({
            "prediction": prediction[0]
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)