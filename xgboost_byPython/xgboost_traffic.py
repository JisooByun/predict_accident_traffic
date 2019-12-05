import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import joblib

data = pd.read_csv('./df_busan_group.csv',names = ["index","Gucode","X","Y","light_num","cross_num","subway_num","school_num","land_value","center_div","island","limit_vel","road_num","road_size","load_length","acc_num"])
del data["index"]
del data["Gucode"]
data = data.drop(0,0)

print(data.dtypes)
print(data.columns)
data[data.columns] = data[data.columns].apply(pd.to_numeric, downcast='float', errors='coerce')
print(data.dtypes)
X, y = data.iloc[:,:-1],data.iloc[:,-1]
data_dmatrix = xgb.DMatrix(data=X,label=y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)
xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 3, alpha = 10, n_estimators = 4000)
xg_reg.fit(X_train,y_train)
joblib.dump(xg_reg,"model01")
preds = xg_reg.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))

#data = data.dropna(how = 'any')
#print(data)
# params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1,
#                 'max_depth': 5, 'alpha': 10}
# cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3,
#                     num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)
# cv_results.head()
# print((cv_results["test-rmse-mean"]).tail(1))
# xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)

xgb.plot_importance(xg_reg)

plt.show()