from flask import Flask, render_template
from flask import request
from flask import jsonify
import numpy as np
import pickle

class model:
    def __init__(self, age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall) -> None:
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trtbps = trtbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalachh = thalachh
        self.exng = exng
        self.oldpeak = oldpeak
        self.slp = slp
        self.caa = caa
        self.thall = thall

        self.data = np.array([[self.age, self.sex, self.cp, self.trtbps, self.chol, self.fbs, self.restecg, self.thalachh, self.exng, self.oldpeak, self.slp, self.caa, self.thall]])

    def calculate(self) -> bool:
        try:
            try:
                ml = pickle.load(open('model.pkl', 'rb'))
            except:
                return "can not load model"
            return ml.predict(self.data)[0]
        except:
            return "an error occurred during computation please check your provided values"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/",  methods = ['GET'])
def api():
    age = request.args.get('age', type=int)
    sex = request.args.get('sex', type=int)
    cp = request.args.get('cp', type=int)
    trtbps = request.args.get('trtbps', type=int)
    chol = request.args.get('chol', type=int)
    fbs = request.args.get('fbs', type=int)
    restecg = request.args.get('restecg', type=int)
    thalachh = request.args.get('thalachh', type=int)
    exng = request.args.get('exng', type=int)
    oldpeak = request.args.get('oldpeak', type=float)
    slp = request.args.get('slp', type=int)
    caa = request.args.get('caa', type=int)
    thall = request.args.get('thall', type=int)

    val = model(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall).calculate()
    if val in [0,1]:
        return jsonify({
                "result": int(val)
            })
    else:
        return jsonify({
                "result": val
            })

if __name__ == '__main__':
    app.run(debug=False)