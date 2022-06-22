import requests
import json
import re
import csv
from os.path import exists
import pandas as pd
from constant import BLOCKLIMIT, FILENAME 

#block, time, quantity, sender, reciver
"""
    This file provide utility function
"""


# Call the url and return data as object
def callAPI(url):
    a = requests.get(url)
    decoded = a.content.decode("utf-8")
    pretty = json.loads(decoded)
    return pretty


def getData(i):
        # Sender and reciver
        b = [m.start() for m in re.finditer('address_hash_link', i)]
        sender =i[b[0]+34:b[0]+76]
        reciver = i[b[1]+34:b[1]+76]
        #print(sender)
        #print(reciver)

        # Transfer quantity
        pos = i.find('<span class="tile-title">')
        quantity = ""
        for el in repr(i[pos+25: pos+100]):
            if el == "<": break
            try:
                float(el)
            except ValueError:
                continue
            quantity += el
        #print(quantity)

        # Block number
        pos = i.find('/block')
        block = ""
        for el in repr(i[pos: pos+100]):
            if el == ">": break
            try:
                float(el)
            except ValueError:
                continue
            block += el
        # tile-title
        #print(block)

        # Data
        pos = i.find("data-from-now=")
        time = i[pos+15: pos+42]

        return ({
            "block": block,
            "time": time,
            "quantity": quantity,
            "sender": sender,
            "reciver": reciver
        })


def getLastBlock():
    checkFileExist()
    with open(FILENAME, "r") as file:
        csvreader =  csv.reader(file)
        head = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
        if data:
            lastblock = data[-1][0]
        else:
            lastblock = BLOCKLIMIT
    return lastblock

def checkFileExist():
    file_exists = exists(FILENAME)
    if file_exists: return
    with open(FILENAME, "w+") as file:
        file.write("block,time,ammount,sender,reciver\n")

def removeDuplicate():
    with open(FILENAME) as f:
        file = f.readlines()
    with open(FILENAME, "w+") as f:
        # remove duplicate
        a = pd.Series(file).drop_duplicates().tolist()
        f.writelines(a)

if __name__ == "__main__":
    checkFileExist()
    removeDuplicate()
    print(getLastBlock())