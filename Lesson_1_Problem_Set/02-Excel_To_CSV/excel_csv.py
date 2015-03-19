# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    loadTimes = sheet.col_values(0, start_rowx=1)
    
    data = []
    for col in range(1,sheet.ncols):
        coldata = []
        station = sheet.col_values(col)[0]
        coldata.append(station)
        sortedCol = sorted(enumerate(sheet.col_values(col, start_rowx=1)), key=lambda selCol: selCol[1])
        ldTime, maxLoad = sortedCol[-1]
        timeStation = xlrd.xldate_as_tuple(loadTimes[ldTime],0)
        coldata.extend(list(timeStation)[:4])
        coldata.append(maxLoad)
        data.append(coldata)
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data

def save_file(data, filename):
    with open(filename, 'wb') as csvfile:
        stationdataWriter = csv.writer(csvfile, delimiter='|')
        stationdataWriter.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for station in data:
            stationdataWriter.writerow(station)
            

    
def test():
#     open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]
#                     print 'pass, field: {}'.format(field)

        
test()

## Udacity solution
# def parse_file(datafile):
#     workbook = xlrd.open_workbook(datafile)
#     sheet = workbook.sheet_by_index(0)
#     data = {}
#     # process all rows that contain station data
#     for n in range (1, 9):
#         station = sheet.cell_value(0, n)
#         cv = sheet.col_values(n, start_rowx=1, end_rowx=None)
# 
#         maxval = max(cv)
#         maxpos = cv.index(maxval) + 1
#         maxtime = sheet.cell_value(maxpos, 0)
#         realtime = xlrd.xldate_as_tuple(maxtime, 0)
#         data[station] = {"maxval": maxval,
#                          "maxtime": realtime}
# 
#     print data
#     return data
# 
# def save_file(data, filename):
#     with open(filename, "w") as f:
#         w = csv.writer(f, delimiter='|')
#         w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
#         for s in data:
#             year, month, day, hour, _ , _= data[s]["maxtime"]
#             w.writerow([s, year, month, day, hour, data[s]["maxval"]])