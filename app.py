from flask import Flask, render_template
from flask import request
from flask import jsonify
import module.model as model

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

    val = model.model(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall).calculate()
    if val in [0,1]:
        return jsonify({
                "result": int(val)
            })
    else:
        return jsonify({
                "result": val
            })

if __name__ == '__main__':
    app.run(debug=True)