from google.colab import data_table
data_table.enable_dataframe_formatter()
from IPython.display import display
# pd.options.display.max_columns = None
# pd.options.display.max_seq_items = 2000
df= pd.read_csv("/content/drive/MyDrive/mitbih_train.csv")
df= pd.DataFrame(df)
# print(df.shape)

x=df.drop(['0.000000000000000000e+00.88'], axis=1)
y=df['0.000000000000000000e+00.88']

# m = df.astype(bool).sum(axis=1)
m = np.count_nonzero(x, axis=1)
s = sum(m)
mi = min(m)
avg = s / 87554 
# x = np.where(m == mi)
df.drop(df.iloc[:, int(avg):187], inplace = True, axis = 1)

display(df)
print("list")
print(m)
print("Average Length")
print(int(avg))
print("min number of non zero")
print(mi)
print("index of row that has minmum number of nonzero")
# print(x)
#np.count_nonzero(df, axis=1)
