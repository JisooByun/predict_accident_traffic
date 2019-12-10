import json
import os

file = open("csvfile/강북구교차로(07~18).csv", "w+")
t4 = ["X","Y","사고번호","발생날짜","발생시간","발생요일","시구동","사고내용","사망자수","중상자수","경상자수","부상신고수",
      "사고유형1","사고유형2","법규위반","노면상태","기상상태","도로형태"]
t5 = ','.join(t4)

file.write(t5+"\n")
def xlcreate(json_name):
    data = json.load(open(json_name,encoding='UTF-8'))
    t1 =[]
    t2 =[]

    for i in range(len(data["features"])):
        keys = ["acdnt_no","acdnt_dd_dc","occrrnc_time_dc","dfk_dc","legaldong_name",
                "acdnt_gae_dc","dprs_cnt","sep_cnt","slp_cnt","inj_aplcnt_cnt","acdnt_dc","acdnt_mdc",
                "lrg_violt_1_dc","rdse_sttus_dc","wether_sttus_dc","road_stle_dc"]
        for l in range(2):
            t1.append(str(data["features"][i]["geometry"]["coordinates"][l]))
        for j in keys:

            t1.append(str((data["features"][i]["properties"][j])))
            t2 = ",".join(t1)

        file.write(t2 + "\n")
        t1 = []
path = './'
file_list = os.listdir(path)
t3 = file_list[1:-1]
print(t3)
for c in t3:
    xlcreate(c)