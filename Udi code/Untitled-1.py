#%%
import pandas as pd

path = "Zombie_ORF_Collection_v3.xlsx"
df = pd.read_excel(path, sheet_name="Sheet1")

#set the index to the "x" column
df.set_index("X", inplace=True)

# reshape the dataframe
df = df.stack().reset_index()

# rename the level_1 column to "Index"
df.rename(columns={"level_1": "Index" , 0: "ORF"}, inplace=True)


dfs = [pd.DataFrame(columns=['X', 'Index', 'ORF']) for _ in range(4)]

for i in range(4):
    dfs[i] = df.iloc[i::4, :]
    dfs[i].reset_index(drop=True, inplace=True)

print(dfs[0].head())
print(dfs[0].shape)
print("----")
print(dfs[1].head())
print("----")
print(dfs[2].head())
print("----")
print(dfs[3].head())

# %%
#make 4 df col name is 1 to 12 and row name is A to H
fin = [pd.DataFrame(columns=[i for i in range(1, 13)], index=[chr(i) for i in range(65, 73)]) for _ in range(4)]

#data from dfs to fin
for i in range(4):
    for j in range(8):
        for k in range(12):
            fin[i].iloc[j, k] = dfs[i].iloc[j*12+k, 2]

#all fin to csv name Spli{1-4}.csv
for i in range(4):
    fin[i].to_csv(f"Split{i+1}.csv")


# print(dfs[0].head())
# print(fin[0].head())