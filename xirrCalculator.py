import pandas as pd
import json, pprint
import numpy as np
import ast 
from datetime import datetime
from scipy import optimize 
import warnings
warnings.filterwarnings("ignore")

df = pd.read_excel('IRR_1.xlsx',parse_dates=False, date_parser=None)
print(df['Date'])
df1=pd.to_datetime(df['Date'])
print(df1)
result = pd.concat([df1, df['Amount']], axis=1, sort=False)
print(result)
res=result.to_json(orient='records',date_format='iso')
res = ast.literal_eval(res)
print(res)
def data_coll():
    final=[]
    for i in res:
        # print(i)
        date_time_str=(i['Date'])[0:10]
        # print(date_time_str)
        amount=(i['Amount'])
        try:
            date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d")
            print(date_time_obj)
        except ValueError:
            date_time_str=(i['Date'])[0:10]
            print("......",type(date_time_str))
            reverse_date = date_time_str[::-1]
            date_time_obj = datetime.strptime(reverse_date,  "%Y-%m-%d")
        finally:
            final.append((date_time_obj,amount))

    return final

def xnpv(rate,cashflows):

    chron_order = sorted(cashflows, key = lambda x: x[0])
    t0 = chron_order[0][0] #t0 is the date of the first cash flow
    print(t0)
    #return sum([cf/(1+r)**((t-t0).days/365.0) for (t,cf) in chron_order])
    #hard coding the rate value to 22.
    return sum([cf/(1+22)**((t-t0).days/365.0) for (t,cf) in chron_order])
    
def xirr(cashflows,guess=0.1): 
        result = optimize.newton(lambda r: xnpv(r,cashflows),guess)
        print("Xirr Value is:",result)
    # except (RuntimeWarning, OverflowError):  
    #     result =optimize.brentq(lambda r: xnpv(r,cashflows),guess, 1e20)
xirr(data_coll())