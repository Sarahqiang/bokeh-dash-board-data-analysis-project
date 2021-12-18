import pandas as pd
data = pd.read_csv("/Users/yaoqiangwu/PycharmProjects/pythonProject/venv/nyc_311_limit1.csv",low_memory=False)
data = data[['1','2','8']]
print(pd.to_datetime(data['2']))
data['time']=((pd.to_datetime(data['2'])-pd.to_datetime(data['1']))).dt.total_seconds()/3600
data['month']=pd.DatetimeIndex(data['1']).month
print(len(data))
data = data[['8','time','month']]
print(len(data))
data = data.groupby(['month'],as_index=False)['time'].mean()
print(data)
#data.to_csv('newresult.tsv',sep="\t",index=False)




#time =pd.to_datetime(data[2])-pd.to_datetime(data[1])
#data = data[time]
#time_differ = (pd.to_datetime(data[2])-pd.to_datetime(data[1])
#data = data[data[8].notna()]
#data = data[pd.to_datetime(data[2])>=pd.to_datetime(data[1])]



