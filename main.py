from flask import Flask,render_template,request
import json
import pickle

with open("model.pickle","rb")as f:
    model=pickle.load(f)

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=request.form
    
    CRIM=float(data["CRIM"])
    ZN=float(data["ZN"])
    INDUS=float(data["INDUS"])
    CHAS=float(data["CHAS"])
    NOX=float(data["NOX"])
    RM=float(data["RM"])
    AGE=float(data["AGE"])
    DIS=float(data["DIS"])
    RAD=float(data["RAD"])
    TAX=float(data["TAX"])
    PTRATIO=float(data["PTRATIO"])
    B=float(data["B"])
    LSTAT=float(data["LSTAT"])
    
    user_input=[[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]]
    
    prediction=model.predict(user_input)
    
    return render_template("index.html",result=prediction)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)