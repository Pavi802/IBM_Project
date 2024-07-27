from flask import Flask ,render_template,request
from math import ceil
app = Flask(__name__)
import pickle
k=open("university.pkl","rb")
model = pickle.load(k)
@app.route("/index")
def index():
    return render_template('predict.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        gre=(float(request.form["gre"])-290)/(340-290)
        tofl=(float(request.form["tofl"])-92)/(120-92)
        rating=(float(request.form["rating"])-1.0)/4.0
        sop=(float(request.form["sop"])-1.0)/4.0
        lor=(float(request.form["lor"])-1.0)/4.0
        cgpa=(float(request.form["cgpa"])-290.0)/(340.0-290.0)
        research=request.form["research"]
        if (research=="Yes"):
             research=1
        else:
             research=0
        preds=[[gre,tofl,rating,sop,lor,cgpa,research]]
        xx=model.predict(preds)
        if (xx>0.5):
            return render_template("chance.html",p=str(ceil(xx[0]*100))+"%")
        return render_template("NoChance.html")
if __name__=='__main__':
    app.run()
