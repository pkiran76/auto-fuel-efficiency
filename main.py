from flask import Flask,request,jsonify  #jsonify is for creating the response
from model_files.ml_model import predict_mpg
import pickle

app=Flask("mpg_prediction")

# @app.route("/",methods=["GET"])
# def ping():
#     return "Pinging Model Appln"

@app.route("/",methods=["POST"])
def predict():
    vehicle_config=request.get_json() #to capture all the data from the request

    with open("./model_files/model.bin","rb") as f_in:
        model=pickle.load(f_in)
        f_in.close()
    predictions=predict_mpg(vehicle_config,model)

    response={"mpg_predictions":list(predictions)}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)