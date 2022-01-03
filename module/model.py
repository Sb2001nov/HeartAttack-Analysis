import numpy as np
import pickle
import os

cwd = os.getcwd()

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
            with open(f"{cwd}/module/model.pkl", "rb") as file:
                ml = pickle.load(file=file)
            return ml.predict(self.data)[0]
        except:
            return "error occurred during computation"



if __name__ == "__main__":
    #test
    obj = model(63, 1, 0, 145, 233, 1, 0, 150, 1, 2.3, 0, 0, 1)
    print(obj.calculate())