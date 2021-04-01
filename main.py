import csv
import codecs
import urllib.request
import sys

# Project from www.visualcrossing.com

BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/'

print('')
print(' - Requesting weather for: ', sys.argv[1])


Location = '&location=' + urllib.parse.quote(sys.argv[1])

WeatherQueryType = sys.argv[2].upper()

QueryKey = '&key' + sys.argv[3]

HistFromDate = sys.argv[4]
HistToDate = sys.argv[5]

if WeatherQueryType == 'FORECAST':
    print(' - Fetching forecast data')
    QueryTypeParams = 'forecast?&aggregateHours=24$unitGroup=us&shortColumnNames=false'
else:
    print(' - Fetching historical data: ',HistFromDate, '-', HistToDate)

QueryDate = '&startDateTime=' + HistFromDate + 'T00:00:00&endDateTime=' + HistToDate + 'T00:00:00'
QueryTypeParams = 'history?&aggregateHours=24&unitGroup=us&dayStartTime=0:0:00&dayEndTime=0:0:00' + QueryDate

URL = BaseURL + QueryTypeParams + Location + QueryDate

print(' - Running query URL: ', URL)
print()

CSVBytes = urllib.request.urlopen(URL)
CSVText = csv.reader(codecs.iterdecode(CSVBytes, 'utf-8'))

RowIndex = 0

for Row in CSVText:
    if RowIndex == 0:
        FirstRow = Row
    else:
        print('Weather in ', Row[0], ' on ', Row[1])

        ColIndex = 0
        for Col in Row:
            if ColIndex >= 4:
                print('   ', FirstRow[ColIndex], ' = ', Row[ColIndex])
            ColIndex += 1
    RowIndex += 1


if RowIndex == 0:
    print('Sorry, but it appears that there was an error connecting to the weather server.')
    print('Please check your network connection and try again..')

if RowIndex == 1:
    print('Sorry, but it appears that there was an error retrieving the weather data.')
    print('Error: ', FirstRow)

print()