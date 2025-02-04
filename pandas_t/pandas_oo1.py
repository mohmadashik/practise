import pandas as pd 

data = {'Name':['ramu','ashik'],'age':[160000,16]}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('file.csv')
df.to_csv('file1.csv',index=True)


