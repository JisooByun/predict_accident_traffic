import pymysql
import pandas as pd

connection = pymysql.connect('localhost' ,'root','123123','dev')
cursor = connection.cursor()

drop_table = """DROP TABLE traffic;"""
creat_table = """CREATE TABLE traffic(id INT(11) NOT NULL AUTO_INCREMENT, gu_code VARCHAR(30) NOT NULL, Longitude FLOAT(12,8) NOT NULL, Latitude FLOAT(12,8) NOT NULL, trafficlight_num INT(11) NOT NULL, crosswalk_num INT(11) NOT NULL, station_num INT(11) NOT NULL, school_num INT(11) NOT NULL, avg_landprice FLOAT(20,10) NOT NULL, house_1 FLOAT(20,5) NOT NULL, house_2 FLOAT(20,10) NOT NULL, house_3 FLOAT(20,10) NOT NULL, house_4 FLOAT(20,10) NOT NULL, commerce_1 FLOAT(20,10) NOT NULL, commerce_2 FLOAT(20,10) NOT NULL, commerce_3 FLOAT(20,10) NOT NULL, commerce_4 FLOAT(20,10) NOT NULL, green_1 FLOAT(20,10) NOT NULL, green_2 FLOAT(20,10) NOT NULL, green_3 FLOAT(20,10) NOT NULL, industry_1 FLOAT(20,10) NOT NULL, industry_2 FLOAT(20,10) NOT NULL, industry_3 FLOAT(20,10) NOT NULL, limit_num FLOAT(20,10) NOT NULL, mediansep_num FLOAT(20,10) NOT NULL, island_num FLOAT(20,10) NOT NULL, mean_lane FLOAT(20,10) NOT NULL, mean_maxspeed FLOAT(20,10) NOT NULL, mean_roadwth FLOAT(20,10) NOT NULL, mean_roadlen FLOAT(20,10) NOT NULL, busstop_num INT(11) NOT NULL, acc_count INT(11) NOT NULL,PRIMARY KEY(id));
"""

cursor.execute(drop_table)
cursor.execute(creat_table)

# data = pd.read_csv('./df_busan_group.csv',
#                    names=["index", "Gu_code", "X", "Y", "light_num", "cross_num", "subway_num", "school_num",
#                           "land_value", "center_div", "island", "limit_vel", "road_num", "road_size", "load_length",
#                           "acc_num"])
# del data["index"]
# data = data.drop(0, 0)
# data[data.columns[1:]] = data[data.columns[1:]].apply(pd.to_numeric, downcast='float', errors='coerce')
# insert_data = """insert into dev(%s) value(%f)"""
# for col in data.columns[1:]:
#     for i in range(len(data[col])):
#         cursor.execute(insert_data, (col, data[col][i + 1]))

connection.commit()
connection.close()
