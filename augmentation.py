from sklearn.utils import resample
class_0=df[df['0.000000000000000000e+00.88']==0.0]
class_1=df[df['0.000000000000000000e+00.88']==1.0]
class_2=df[df['0.000000000000000000e+00.88']==2.0]
class_3=df[df['0.000000000000000000e+00.88']==3.0]
class_4=df[df['0.000000000000000000e+00.88']==4.0]
df = pd.concat([class_1, class_2, class_3, class_4, class_0])

class_1_upsample = resample(class_1, n_samples = 20000, replace = True, random_state = 123)
class_2_upsample = resample(class_2, n_samples = 20000, replace = True, random_state = 123)
class_3_upsample = resample(class_3, n_samples = 20000, replace = True, random_state = 123)
class_4_upsample = resample(class_4, n_samples = 20000, replace = True, random_state = 123)
class_0_downsample = resample(class_0, n_samples = 20000, replace = True, random_state = 123)
df = pd.concat([class_1_upsample, class_2_upsample, class_3_upsample, class_4_upsample, class_0_downsample])

plt.figure(figsize= (10,10))
my_circle = plt.Circle((0,0), 0.7, color = 'white') 
plt.pie(df['0.000000000000000000e+00.88'].value_counts(), labels=['Normal Beats','Unknown Beats','Ventricular ectopic beats','Supraventricular ectopic beats','Fusion Beats'], autopct = '%0.0f%%', colors = ['red','orange','blue','magenta','cyan'])
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

display(df)
