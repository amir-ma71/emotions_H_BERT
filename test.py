# from src.HebEMO import *
#
# HebEMO_model = HebEMO()
#
# # HebEMO_model.hebemo(input_path = 'examples/text_example.txt')
# # return analyzed pandas.DataFrame
# txt = "נקודת המבט הישראלית בבחירתו מחדש של אורבן מעניינת בעיקר משום תמיכתו הבלתי מתפשרת של אורבן בישראל במוסדות האיחוד האירופי "
# hebEMO_df = HebEMO_model.hebemo(
#     text=txt)
#
# print(hebEMO_df)
#
# # import pandas as pd
# # ddf = pd.read_csv("./HeBERT/data/covid_main_raw_to_publish.csv", encoding="utf-8")
# # print(6)

d = {"esm":[], "do":[]}
deleted_keys=[]
for i in d.keys():
    if len(d[i]) == 0:
        deleted_keys.append(i)

for j in deleted_keys:
    del d[j]
print(d)