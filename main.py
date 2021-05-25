import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

cols = [
    'TEST ID',
    'HEATMAP_MUNICIPALITY',
    'DOWNLOAD SPEED',
    'TEST SERVER'
]
    
df = pd.read_csv ('RMADataForHackathon21-04-23.csv', usecols=cols)
ds = df.sort_values(by=['DOWNLOAD SPEED'], ascending=True, kind='mergesort')

print(ds.head())
         


fp = "Municipal_Boundaries_SHP_Geographic//CITY.shp"

#reading the file stored in variable fp
map_df = gpd.read_file(fp)
map_df.plot()
plt.show()





