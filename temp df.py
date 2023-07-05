import pandas as pd

l1 = [1,2,3,4,5]
l2 = [1,3,5,7,9]

df1 = pd.DataFrame()
df1['Column 1'] = l1
df1['Column 2'] = l2

# df2 = pd.DataFrame()
# df2['Column 1'] = l2
# df2['Column 2'] = l1

df3 = pd.DataFrame([['THIS IS A TEXT', 2], ['ANOTHER TEXT', 4]], columns = ['First column', 'Second'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns= ['First column', 'Second'])

df3 = pd.concat([df3, pd.DataFrame([[5,6]], columns = ['First column', 'Second'])], ignore_index=True)
# df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


# print(df1)
# print(' '*2)
# print(df1.head())

print(df3)
