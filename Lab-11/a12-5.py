import pandas as pd

dates = pd.date_range(start='2025-04-06', periods=10)
df = pd.DataFrame({
    'date': dates,
    'john_visits': [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    'judy_visits': [0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
})

l=[]
for i in range(len(df)):
    j=i
    count=0
    while(df.loc[j]['john_visits']&df.loc[j]['judy_visits'] != True):
        count+=1
        j+=1
    l.append(count)
df['no_of_days_till_party'] = pd.Series(l)
print(df)