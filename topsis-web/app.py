import os
from flask import Flask, request
import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage

# Flask app
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "templates"))

# ---------------- TOPSIS FUNCTION ----------------
def topsis(df, weights, impacts):
    data = df.iloc[:, 1:].astype(float)
    weights = np.array(weights, dtype=float)

    norm = np.sqrt((data ** 2).sum())
    weighted = (data / norm) * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_worst / (d_best + d_worst)
    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False).astype(int)

    return df

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    with open(os.path.join("templates", "index.html"), "r", encoding="utf-8") as f:
        return f.read()

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    weights = request.form["weights"].split(",")
    impacts = request.form["impacts"].split(",")
    email = request.form["email"]

    # Validations
    if len(weights) != len(impacts):
        return "Error: Number of weights and impacts must be equal"

    for i in impacts:
        if i not in ['+', '-']:
            return "Error: Impacts must be + or - only"

    df = pd.read_csv(file)
    result = topsis(df, weights, impacts)

    output_file = "result.csv"
    result.to_csv(output_file, index=False)

    # ---------------- EMAIL SETUP ----------------
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "sarang.priani2@gmail.com"
    msg["To"] = email
    msg.set_content("Please find the attached TOPSIS result file.")

    with open(output_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("sarang.priani2@gmail.com", "APP_PASSWORD")
            server.send_message(msg)
        return "Result generated and sent to email successfully"

    except Exception:
        return "Result generated successfully. Email could not be sent due to network restrictions."

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(debug=True)

