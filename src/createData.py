import csv
import json
import datetime
from dateutil.relativedelta import relativedelta
from constant import FILENAME

DATAFOLDER = "../data"

'''
    Generate file
'''
def getData(timeMin, timeMax):
    with open(FILENAME) as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        good = []
        for row in csvreader:
            row[1] = row[1].removesuffix(".000000Z")
            date_obj = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
            if timeMax > date_obj and date_obj > timeMin:
                good.append(row)
    jsonData = []
    for d in good:
        jsonData.append({
            "block": d[0],
            "data": d[1],
            "ammount": d[2],
            "sender": d[3],
            "reciver": d[4]
        })
    return jsonData


def generateYear():
    years = range(2020, datetime.date.today().year+1)
    for year in years:
        timeMin = datetime.datetime.strptime(str(year), "%Y")
        timeMax = timeMin + relativedelta(years=1)
        data = getData(timeMin, timeMax)
        with open(f"{DATAFOLDER}/year/{year}.json", "w+") as file:
            json.dump(data, file, indent=4)

def generateMonth():
    years = range(2020, datetime.date.today().year+1)
    months = [str(i).rjust(2, "0") for i in range(1, 13)]
    for year in years:
        for month in months:
            if year == 2020 and int(month) != 12: continue
            timeMin = datetime.datetime.strptime(f"{year}:{month}", "%Y:%m")
            timeMax = timeMin + relativedelta(months=1)
            data = getData(timeMin, timeMax)
            if year == datetime.date.today().year and month == str(datetime.date.today().month + 1).rjust(2, "0"): return
            with open(f"{DATAFOLDER}/month/{year}_{month}.json", "w+") as file:
                json.dump(data, file, indent=4)


def generateLast():
    # last month
    timeMax = datetime.datetime.today()
    timeMin = timeMax - relativedelta(months=1)
    data = getData(timeMin, timeMax)
    with open(f"{DATAFOLDER}/last/month.json", "w+") as file:
        json.dump(data, file, indent=4)
    # last 3month
    timeMax = datetime.datetime.today()
    timeMin = timeMax - relativedelta(months=3)
    data = getData(timeMin, timeMax)
    with open(f"{DATAFOLDER}/last/3month.json", "w+") as file:
        json.dump(data, file, indent=4)
    # last 6month
    timeMax = datetime.datetime.today()
    timeMin = timeMax - relativedelta(months=6)
    data = getData(timeMin, timeMax)
    with open(f"{DATAFOLDER}/last/6month.json", "w+") as file:
        json.dump(data, file, indent=4)
    # last year
    timeMax = datetime.datetime.today()
    timeMin = timeMax - relativedelta(months=12)
    data = getData(timeMin, timeMax)
    with open(f"{DATAFOLDER}/last/year.json", "w+") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    #generateYear()
    #generateMonth()
    #generateLast()
    exit()
