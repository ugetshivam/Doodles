import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
df_1 = pd.read_csv("gdp.csv", skiprows = 4)
df_1.drop('Country Code',axis = 1, inplace = True)
df_1.drop('Indicator Code',axis = 1, inplace = True)
df_1.set_index('Country Name', inplace = True)
df_1 = df_1[[str(x) for x in range(2015, 2019)]]
df_2 = pd.read_csv("gni.csv", skiprows=4)
df_2.drop('Country Code',axis = 1, inplace = True)
df_2.drop('Indicator Code',axis = 1, inplace = True)
df_2.set_index('Country Name', inplace = True)
df_2 = df_2[[str(x) for x in range(2015, 2019)]]
df_2.dropna(inplace = True)
df_1.dropna(inplace = True)
gdp = pd.DataFrame(index = df_1.columns, columns = ['India',  'United States', 'China'])
gdp['India'] = df_1.loc['India']
gdp['United States'] = df_1.loc['United States']
gdp['China'] = df_1.loc['China']
# gdp = gdp.T
gni = pd.DataFrame(index = df_1.columns, columns = ['India',  'United States', 'China'])
gni['India'] = df_2.loc['India']
gni['United States'] = df_2.loc['United States']
gni['China'] = df_2.loc['China']
# gdp
# gni = gni.T
index = np.arange(2015,2019)
plt.figure(figsize = (10,8))
bar_width = 0.35

plt.subplot(131)
plt.bar(index - bar_width/2,gdp['India'], bar_width, label = 'GDP')
plt.bar(index + bar_width/2, gni['India'], bar_width, label = 'GNI')
plt.xticks(index, rotation = 30)
plt.ylabel("GDP/GNI(Current US $)")
plt.title("INDIA")
plt.legend()

plt.subplot(132)
plt.bar(index - bar_width/2,gdp['United States'], bar_width)
plt.bar(index + bar_width/2, gni['United States'], bar_width)
plt.xticks(index, rotation = 30)
plt.title("UNITED STATES")

plt.subplot(133)
plt.bar(index - bar_width/2,gdp['China'], bar_width)
plt.bar(index + bar_width/2, gni['China'], bar_width)
plt.xticks(index, rotation = 30)
plt.title("CHINA")

plt.show()
