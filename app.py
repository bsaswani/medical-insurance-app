from flask import Flask, render_template, request
import pickle
import numpy as np

# Load your trained CatBoost model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        # Get form values
        age = int(request.form["age"])
        sex = request.form["sex"]
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]

        # Encode categorical values (must match training preprocessing)
        sex = 1 if sex == "male" else 0
        smoker = 1 if smoker == "yes" else 0
        region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
        region = region_dict[region]

        # Create feature array
        features = np.array([[age, sex, bmi, children, smoker, region]])

        # Predict charges
        prediction = model.predict(features)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


