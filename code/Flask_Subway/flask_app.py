from flask import Flask, render_template, request
import numpy as np
import pickle
import os
# 플라스크 앱 생성
app=Flask(__name__)
# 모델 가져오기
path=r'C:\Users\user\Documents\Ai_Class\python\Flask_Subway\subway_rf.pkl'
model=pickle.load(open(path,'rb'))
print(model)

# 플라스크 앱 구동
@app.route('/')
def hello():
    return render_template("start.html")

@app.route('/result',methods=['POST'])
def home():
    subway01=float(request.form['value1'])
    subway02=float(request.form['value2'])
    subway03=float(request.form['value3'])
    data=np.array([subway01,subway02,subway03]).reshape(1,3)
    test_X=data
    pred=model.predict(test_X)

    return render_template("result.html",data=pred)
if __name__=='__main__':
    app.run(debug=True)