# -*- coding: utf-8 -*-
"""Traffic_MachineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_b1LsEtZ9n-xVKk_mVVp658LxWwQLh4c
"""

'''
참고문헌

1. https://www.datacamp.com/community/tutorials/xgboost-in-python
2. http://swlock.blogspot.com/2019/01/xgboost-python.html
3. https://machinelearningmastery.com/feature-importance-and-feature-selection-with-xgboost-in-python/
4. https://blog.naver.com/bosongmoon/221574787121
5. https://frhyme.github.io/python-lib/plt_hist/
6. https://financedata.github.io/posts/faq_matplotlib_default_chart_size.html
7. https://www.tutorialspoint.com/permutation-and-combination-in-python
'''

# from google.colab import drive
# drive.mount('/content/drive')

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import joblib

plt.rcParams["figure.figsize"] = (30,12)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'Green'
plt.rcParams['axes.grid'] = True

#특정 경로에서 불러오고, 컬럼명 확인하기

df = pd.read_csv("Seoul_Busan_Data.csv", encoding = 'UTF-8')
print(df.columns)

#필요없는 컬럼 삭제 및 중복Data 결합_사고건수 기준 학습용(axis=o이면 row, axis=1이면 column / inplace=True는 drop후의 df로 기존 df를 대체한다는 의미, 즉 기본값)

print(df.shape)

df.drop(['NODE_NAME','Longitude','Latitude','X','Y','si_code','gu_code','acc_X','acc_Y','acc_num','acc_day','acc_time','acc_date','acc_content',
         'injury_1','injury_2','injury_3','injury_4','acc_type1','acc_type2','violate','road_cond','weather'], axis = 1, inplace = True)
df = df.drop_duplicates('NODE_ID', keep = 'first')
#drop_duplicate는 필히 변수에 새로 저장해줘야 하고, 그냥 drop은 변수에 저장하면 오히려 에러뜸

df.head(3)
print(df.shape)
print(df.columns)

df.drop('NODE_ID', axis = 1, inplace = True)

df.head(3)
print(df.shape)
print(df.columns)

#dtype = object 를 dtype = float로 변환
#df[df.columns] = df[df.columns].apply(pd.to_numeric, downcast='float', errors='coerce')

from warnings import simplefilter

#FutureWarning이 눈에 거슬리므로, 출력되지 않도록 한다.

simplefilter(action='ignore', category=FutureWarning)

'''전처리 마지막(저장코드)
data.to_csv("./Busan_FinalData.csv")'''

#루트를 취한 사고값 컬럼 추가

root_acc = []

for acc in df.iloc[:, -1]:
 df.acc = root_acc.append(np.sqrt(acc))
df['root_acc'] = root_acc

print(df.iloc[:,-1])

#X는 독립변수, y는 종속변수(사고건수)
#df.iloc[:, n] => n = -1이면 루트사고건수, n = -2이면 원사고건수

X,y = df.iloc[:,:-2], df.iloc[:,-1]
data_dmatrix = xgb.DMatrix(data = X, label = y)

#무작위로 trainset, testset 뽑아내기

from sklearn.model_selection import train_test_split

#train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)순으로 작성, Validation set이 필요하다면, 기존에 나눈 것을 같은 함수로 한번 더 나눠야

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

#xgboooooooooooooooooost

xg_reg = xgb.XGBRegressor(objective = 'reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                         max_depth = 3, alpha = 10, n_estimators = 1000)

xg_reg.fit(X_train,y_train)
preds = xg_reg.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" %(rmse))
print(xg_reg.feature_importances_)

#시각화(1)

plt.bar(range(len(xg_reg.feature_importances_)), xg_reg.feature_importances_)
plt.show()

#시각화(2)

xgb.plot_importance(xg_reg)
plt.figure(figsize=(12,3))
plt.show()

joblib.dump(xg_reg,"xg_reg_003")