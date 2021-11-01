import pickle
import numpy as np
from flask import Flask, request, jsonify


with open("dv.bin", "rb") as file_in:
    dv = pickle.load(file_in)

with open("model.bin", "rb") as file_in:
    model = pickle.load(file_in)
    
    
app = Flask("/sales_prediction")

@app.route("/sales_prediction", methods=["POST"])
def sales_prediction():
    product = request.get_json()
    X_product = dv.transform(product)
    result = {
        "predicted_sales" : np.expm1(model.predict(X_product)).round(0)[0]
    }
    return(jsonify(result))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)