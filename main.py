import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import sqlite3
import sqlalchemy
from sqlalchemy.orm import sessionmaker

TOKEN = 'RmlNdmZScvGusDeGMRjQGNMDdKxhKdJv'
STATION_ID = 'GHCND:USW00023129'
DATABASE_LOCATION = "sqlite:///WeatherData.db"

dates_temp = []
dates_prcp = []
temps = []
prcp = []

for year in range(2016, 2017):
    year = str(year)
    print('retreiving ' + year + ' data')

    # make the api call
    r = requests.get(
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=GHCND:USW00023129&startdate=' + year + '-01-01&enddate=' + year + '-12-31',
        headers={'token': TOKEN})
    # load the api response as a json
    d = json.loads(r.text)

    # get all items in the response which are average temperature readings
    avg_temps = [item for item in d['results'] if item['datatype'] == 'TAVG']
    # get the date field from all average temperature readings
    dates_temp += [item['date'] for item in avg_temps]
    # get the actual average temperature from all average temperature readings
    temps += [item['value'] for item in avg_temps]

print(avg_temps[1])


