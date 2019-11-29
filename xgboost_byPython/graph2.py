import json

data = json.load(open("data2.json",encoding='UTF-8'))
#
# i_0 = []
# i_1 =[]
# i_2 =[]
# i_3 =[]
# i_4 =[]
index_list = []
for j in range(6):
    index_list.append("variable"+str(j))
print(index_list)
print(data[0]["-2"])
for k,t in zip(["-2","-1",'0','1','2'],[0,1,2,3,4]):
    s = "i_"+str(t)
    s = str(s)
    s = []
    for i in range(6):

        s.append(data[i][k])





    M = dict(zip(index_list, s))
    json.dumps(M)

    print(M)

