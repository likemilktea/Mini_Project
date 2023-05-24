import pickle # 모델 학습 후 저장 파일 만들기
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

#  데이터 불러오기 
subway_df = pd.read_csv(r"seoul_subway.csv",encoding="cp949")

subway_changed_line=subway_df.copy()
subway_changed_line['호선명'] = subway_changed_line['호선명'].map({'1호선':1, '2호선':2, '3호선':3, '4호선':4, '5호선':5, '6호선':6, '7호선':7, '8호선':8, '9호선':9,
       '9호선2~3단계':10, '경강선':11, '경부선':12, '경원선':13, '경의선':14, '경인선':15, '경춘선':16, '공항철도 1호선':17,
       '과천선':18, '분당선':19, '수인선':20, '신림선':21, '안산선':22, '우이신설선':23, '일산선':24, '장항선':25, '중앙선':26,
       '9호선2단계':27})

# 학습 모델
subway_drop = subway_changed_line.drop("07시-08시 하차인원", axis=1)
subway_drop = subway_drop.drop("작업일자", axis=1)
subway_drop = subway_drop.set_index("지하철역")
columns=['사용월', '호선명','07시-08시 승차인원']
subway_drop=subway_drop[columns]
print(subway_drop)

# 테스트 모델
subway_down = subway_changed_line['07시-08시 하차인원']

# 데이터 나누기
X_train,X_test,y_train,y_test=train_test_split(subway_drop, subway_down, test_size=0.25, random_state=42)

# 모델 지정 및 학습 
model = LinearRegression()
model.fit(X_train, y_train)

pred=model.predict(X_test)
r2 = r2_score(y_test, pred)
print('R2 score :', r2)

#데이터 저장
pickle.dump(model, open('subway_rf.pkl', 'wb'))

