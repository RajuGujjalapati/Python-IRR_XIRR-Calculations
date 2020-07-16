import pandas as pd
import json, pprint
import numpy as np
import ast 
df = pd.read_excel('IRR_1.xlsx')
print(df)
res=df.to_json(orient='records',date_format='iso',date_unit='s')
res = ast.literal_eval(res)
print((res))
final=[]
for i in res:
    # print(i)
    res=(i['Amount'])
    final.append(res)
Solution = np.irr(final) 
print("Internal Rate of Return : ", Solution)  