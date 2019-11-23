import pymysql
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import numpy as np
# Guname = AA,BB,CC..... factor: light_num,schoolnum.... value 1,2,3,10,20....
def return_top5_cross(GuName,factor,value):


    connection = pymysql.connect('localhost' ,'root','123123','dev')

    cursor = connection.cursor()
    get_Gu = "select * from traffic where gu_code=%s"
    cursor.execute(get_Gu,(GuName))

    datas = cursor.fetchall()
    df = pd.DataFrame(datas, columns =  ["id", "gu_code", "Longitude", "Latitude", "trafficlight_num", "crosswalk_num", "station_num", "school_num", "avg_landprice", "house_1", "house_2", "house_3", "house_4", "commerce_1", "commerce_2", "commerce_3", "commerce_4", "green_1", "green_2", "green_3", "industry_1","industry_2", "industry_3", "limit_num", "mediansep_num", "island_num", "mean_lane", "mean_maxspeed", "mean_roadwth", "mean_roadlen", "busstop_num", "acc_count"])
    print("------------------sql에서 선택된 구만 뽑음------------------")
    print(df)
    df_process = df.iloc[:,4:-1]
    print("------------------factor들만 뽑은 데이터------------------")
    print(df_process)
    df_process[df_process.columns] = df_process[df_process.columns].apply(pd.to_numeric, downcast='float', errors='coerce')

    xgboost_001 = joblib.load('xg_reg_003')

    pred_ori = xgboost_001.predict(df_process)
    df["pred_ori"] = pred_ori
    #여기까지가 요인변경 안한 데이터로 모델에 넣어 얻은 값을 pre_ori 칼럼에 넣음
    print("------------------df에 pre_ori 칼럼추가------------------")
    print(df)
    df_process[factor] = df_process[factor] + value
    for j in range(len(df["gu_code"])):
         if(df_process[factor][j]< 0): #만약 value로 뺏을때 (-) 가 나온다면 그 부분만 0으로 바꿈
             df_process[factor][j] = 0
    print("------------------변경된 factor가 실제로 바뀌었는지 확인------------------")
    print(df[factor])
    print(df_process[factor])
    pred_factor = xgboost_001.predict(df_process)
    df["pred_factor"] = pred_factor
    df["pred-decline"] = df["pred_factor"]-df["pred_ori"]
    df["pred-decline"] = round(df["pred-decline"],2)
    print("------------------요인변경후 예측값, 변경전과 변경후의 차이------------------")
    print(df)
    print(df["Longitude"])
    print(df["Latitude"])
    df["pred_ori2"] = df["pred_ori"]*df["pred_ori"]
    print(df["pred_factor"])
    df = df.sort_values("pred-decline")

    row_num =[]
    for i in range(len(df["gu_code"])): #정렬시킨뒤 순위정해줌
        row_num.append(i+1)
    df["rank"]= row_num
    print("------------------rank 추가된 데이터프레임------------------")
    print(df)

    x = df.loc[df["rank"].isin([1,2,3,4,5,6])]
    print("------------------최종으로 웹에 넘길 상위 6개 데이터------------------")
    print(x)
    rmse = np.sqrt(mean_squared_error(df["pred_ori2"], df["acc_count"]))
    print(rmse)
    json_x = x.to_json(orient='table')
    return json_x
return_top5_cross("AA","trafficlight_num",1) #테스트 데이터