#Plot the position of the ISS over a map of the earth

import pandas as pd

###########################################
#grab the data and convert to a dataframe
file_path = r'C:\Users\John Green\Desktop\iss_location.csv'

def convert_df(file_path):
    iss_df = pd.read_csv(file_path)
    return iss_df

iss_data = convert_df(file_path)
#grab the data and convert to a dataframe
###########################################



###########################################
#convert Timestamp into readable dates...

from datetime import datetime

timestamp = iss_data.iloc[:,0]
time_list = []
def datetime_converter(timestamp_list):
    datetime_convert = datetime.fromtimestamp(timestamp_list)
    str_datetime = datetime_convert.strftime("%Y-%m-%d %H:%M:%S")
    return str_datetime

converted_dates = list(map(datetime_converter , timestamp))
#print(converted_dates)

#convert Timestamp into readable dates...
###########################################



###########################################
#remove any trailing and leading spaces in column names
def remove_space(editing_df):
    new_cols = [i.lstrip().rstrip() for i in editing_df.columns]
    new_cols_dict = dict(zip(editing_df.columns , new_cols))
    editing_df.rename(columns = new_cols_dict , inplace = True)
    return editing_df

remove_space(iss_data)
#remove the trailing and leading spaces in column names
###########################################



###########################################
#add the converted timestamp to a copy of the data

iss_data_copy = iss_data.copy()
converted_dates_df = pd.DataFrame(converted_dates ,columns = ['Time'])

iss_data_copy['Time'] = converted_dates_df['Time']
print(iss_data_copy.head())

#add the converted timestamp to a copy of the data
###########################################



###########################################
#Draw path of ISS over Earth

import plotly.express as px

fig = px.line_mapbox(iss_data_copy , lat = 'Latitude' , lon = 'Longitude' , zoom = 2, height = 300 )
fig.update_layout(mapbox_style = 'statemen-terrain' , mapbox_zoom = 2)
fig.show()

#Draw path of ISS over Earth
###########################################
