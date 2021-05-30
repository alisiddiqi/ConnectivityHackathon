# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Rank areas by internet connection


import pandas as pd
import matplotlib.pyplot as plt
import json

cols = [
    'TEST ID',
    'HEATMAP_MUNICIPALITY',
    'DOWNLOAD SPEED',
    'UPLOAD SPEED',
    'SERVICE TYPE',
    'TEST SERVER'
]

df = pd.read_csv ('RMADataForHackathon21-04-23.csv', usecols=cols)
df = df.drop_duplicates()


# How to find the best overall 

# Find What type of internet usage is possible in which counties
# Ranks Yes or No

# Factors:
    # Mulitple people can use internet at the same time
    # Gaming 
    # Zoom Video calls
    # Watch Netflix HD(1080p)
    # Internet surfing

 #   https://www.reviews.org/internet-service/how-many-mbps-do-i-need/




# %%

ds = df.sort_values(by=['HEATMAP_MUNICIPALITY', 'DOWNLOAD SPEED'], ascending=True, kind='mergesort') # Arrange data by municipalities 
ds = ds[ds["DOWNLOAD SPEED"] > 0 ]
print(ds.head(20))


# %%

ds_avgdwnld = ds.groupby('HEATMAP_MUNICIPALITY', as_index=False)[['DOWNLOAD SPEED']].mean()
# print(ds_avgdwnld)
ds_avgdwnld = ds_avgdwnld.rename(columns={"DOWNLOAD SPEED": "AVG DOWNLOAD SPEED"})
ds_avgdwnld = ds_avgdwnld.sort_values(by=['AVG DOWNLOAD SPEED'], ascending=False, kind='mergesort')

print(ds_avgdwnld[0:60])





# %%
result = ds_avgdwnld.to_json(r'C:\Users\alisi\Desktop\Code\ConnectivityHackathon\data.json',orient="index" )
# parsed = json.loads(result)
# json.dumps(parsed, indent=3)  


# %%
# Find What type of internet usage is possible in which counties
# Ranks Yes or No

# Factors:
    # Mulitple people can use internet at the same time
    # Gaming 
    # Zoom Video calls
    # Watch Netflix HD(1080p)
    # Internet surfing #   https://www.reviews.org/internet-service/how-many-mbps-do-i-need/



# %%
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
from folium.plugins import HeatMap
import shapefile
import json


cols = [
    'ClientCity',
    'TestThroughputMbpsDownload',
    'ClientLat',
    'ClientLong'
]
    
df = pd.read_csv ('./data/2021-04-01_Mlab_data_start.csv', usecols=cols, nrows=5)
df["TestThroughputMbpsDownload"].describe()

print(df)



ds = df.sort_values(by=['ClientCity', 'TestThroughputMbpsDownload'], ascending=True, kind='mergesort')

print(ds)         
fp = "Municipal_Boundaries_SHP_Geographic//CITY.shp"
fp2 = "Municipal_Boundaries_SHP_Geographic//RURAL.shp"
fp3 = "Municipal_Boundaries_SHP_Geographic//OCTEXT.shp"
fp4 = "Municipal_Boundaries_SHP_Geographic//TOWN.shp"
fp5 = "Municipal_Boundaries_SHP_Geographic//urbserv.shp"

fp6 = "Municipal_Boundaries_SHP_Geographic//VILLAGE.shp"
fp7 = "Municipal_Boundaries_SHP_Geographic//SVILLAGE.shp"
fp8 = "Municipal_Boundaries_SHP_Geographic//HAMLETPT.shp"
fp9 = "Municipal_Boundaries_SHP_Geographic//INDIAN.shp"



#reading the file stored in variable fp
map_df = gpd.read_file(fp)
map_df2 = gpd.read_file(fp2)
map_df3 = gpd.read_file(fp3)
map_df4 = gpd.read_file(fp4)

# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
# map_df.plot()

x = map_df.plot(color='red')
y = map_df2.plot(ax=x,color='green', edgecolors='black')
z = map_df3.plot(ax=y,color='pink')
 
map_df4.plot(ax=z, color='none', edgecolors='b')
# plt.show()


# # read the shapefile
# geojson_data = shapefile.Reader('myshpfile.geojson').__geo_interface__
# print(geojson_data)

# read the shapefile
reader = shapefile.Reader(fp9)
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []


# write the GeoJSON file

# for sr in reader.shapeRecords():
#     atr = dict(zip(field_names, sr.record))
#     geom = sr.shape.__geo_interface__
#     buffer.append(dict(type="Feature",     geometry=geom, properties=atr)) 
   
   
# geojson = open("./JSON/INDIAN.json", "w")
# geojson.write(json.dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
# geojson.close()


# %%
#index download speeds be region


# %%
# fp = "Municipal_Boundaries_SHP_Geographic//CITY.shp"

# #reading the file stored in variable fp
map_df = gpd.read_file(fp2)
map_df.to_file('./JSON/rural.geojson', driver='GeoJSON')

# map_df.plot()
# plt.show()


# %%



