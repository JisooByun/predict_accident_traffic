import pandas as pd

data = pd.read_csv('./df_busan_group.csvfile',names = ["index","Gu_code","X","Y","light_num","cross_num","subway_num","school_num","land_value","center_div","island","limit_vel","road_num","road_size","load_length","acc_num"])
del data["index"]
data = data.drop(0,0)
insert_data = """insert into dev(%s) value(%f)"""
for col in data.columns[1:]:
    for i in range(len(data[col])):
        cursor.execute(insert_data,(col, data[col][i+1]))




print(data.columns)
print(len(data['Gu_code']))