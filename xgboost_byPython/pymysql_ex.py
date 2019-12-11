import pymysql
import pandas as pd

connection = pymysql.connect('localhost' ,'root','123123','dev')
cursor = connection.cursor()

drop_table = """DROP TABLE traffic;"""
creat_table = """CREATE TABLE traffic(id INT(11) NOT NULL AUTO_INCREMENT, gu_code VARCHAR(30) NOT NULL, Longitude FLOAT(12,8) NOT NULL, Latitude FLOAT(12,8) NOT NULL, Radius INT(11) NOT NULL, trafficlight_num INT(11) NOT NULL, crosswalk_num INT(11) NOT NULL, station_num INT(11) NOT NULL, school_num INT(11) NOT NULL, land_price FLOAT(20,10) NOT NULL, house_1 FLOAT(20,5) NOT NULL, house_2 FLOAT(20,10) NOT NULL, house_3 FLOAT(20,10) NOT NULL, house_4 FLOAT(20,10) NOT NULL, commerce_1 FLOAT(20,10) NOT NULL, commerce_2 FLOAT(20,10) NOT NULL, commerce_3 FLOAT(20,10) NOT NULL, commerce_4 FLOAT(20,10) NOT NULL, green_1 FLOAT(20,10) NOT NULL, green_2 FLOAT(20,10) NOT NULL, green_3 FLOAT(20,10) NOT NULL, industry_1 FLOAT(20,10) NOT NULL, industry_2 FLOAT(20,10) NOT NULL, industry_3 FLOAT(20,10) NOT NULL, limit_num FLOAT(20,10) NOT NULL, mediansep_ FLOAT(20,10) NOT NULL, island_num FLOAT(20,10) NOT NULL, mean_lanes FLOAT(20,10) NOT NULL, mean_speed FLOAT(20,10) NOT NULL, mean_wth FLOAT(20,10) NOT NULL, mean_loadlen FLOAT(20,10) NOT NULL, busstop_num INT(11) NOT NULL, police_num INT(11) NOT NULL, CtoC_num INT(11) NOT NULL, CtoP_num INT(11) NOT NULL, total_acc INT(11) NOT NULL,PRIMARY KEY(id));
"""
insert_data = """LOAD DATA LOCAL INFILE '/home/byun/Seoul_dataset.csv' INTO TABLE traffic FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id, gu_code, Longitude, Latitude, Radius, trafficlight_num, crosswalk_num, station_num, school_num, land_price, house_1, house_2, house_3, house_4, commerce_1, commerce_2, commerce_3, commerce_4, green_1, green_2, green_3, industry_1, industry_2, industry_3, limit_num, mediansep_, island_num, mean_lanes, mean_speed, mean_wth, mean_loadlen, busstop_num, police_num, CtoC_num, CtoP_num, total_acc);
"""
cursor.execute(drop_table)
cursor.execute(creat_table)
cursor.execute(insert_data)
# data = pd.read_csv('./df_busan_group.csvfile',
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
