import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Charger le modèle préalablement sauvegardé
with open('src/avocado_price_model.pkl', 'rb') as model_file:
    model_pipeline = pickle.load(model_file)

@app.route('/')
def home():
    return "Bienvenue sur l'API de prédiction du prix des avocats !"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées dans la requête POST
        data = request.get_json()

        # Extraire les valeurs de données et les organiser dans un dictionnaire
        feature_data = {
            "Quality1": data["Quality1"],
            "Quality2": data["Quality2"],
            "Quality3": data["Quality3"],
            "Small Bags": data["Small Bags"],
            "Large Bags": data["Large Bags"],
            "XLarge Bags": data["XLarge Bags"],
            "year": data["year"],
            "type": data["type"],
            "region": data["region"]
        }

        # Convertir le dictionnaire en un DataFrame Pandas
        features_df = pd.DataFrame([feature_data])

        # Prédire avec le modèle chargé
        prediction = model_pipeline.predict(features_df)

        # Convertir la prédiction en float pour éviter l'erreur de sérialisation
        predicted_price = float(prediction[0])

        # Retourner la prédiction sous forme de JSON
        return jsonify({"predicted_price": predicted_price})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
