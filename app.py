from flask import Flask, render_template, request
from config import Config
import pandas as pd
import os

app = Flask(__name__)

def load_data():
    all_data = []
    for file in os.listdir(Config.DATA_FOLDER):
        if file.endswith(".xlsx") or file.endswith(".csv"):
            path = os.path.join(Config.DATA_FOLDER, file)
            try:
                df = pd.read_excel(path)
            except:
                df = pd.read_csv(path)
            df['Source File'] = file
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

df_assets = load_data()

@app.route("/", methods=["GET", "POST"])
def index():
    query = request.form.get("query")
    results = None

    if query:
        results = df_assets[
            df_assets.apply(lambda row: query.lower() in str(row.values).lower(), axis=1)
        ]

    return render_template("index.html", result=results, query=query)

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
