import json
import os
from time import sleep
from util import callAPI, getData, getLastBlock, checkFileExist, removeDuplicate
from constant import STARTURL, SLEEPTIME, FILENAME, TEMP

def convertToMain():
    checkFileExist()
    with open(TEMP, "r") as f:
        lines = f.readlines()
        elements = []
        for el in lines:
            elements.append(json.loads(el))
    with open(FILENAME, "a+") as f:
        for el in elements[::-1]:
            f.write(",".join(el.values()))
            f.write("\n")

def download():
    lastblock = getLastBlock()
    url = STARTURL
    transactions = []
    done = 1
    # clear of create the temp file
    with open(TEMP, "w+") as file:
        file.truncate(0)

    # loop until all blocks has been downloaded
    while True:
        try:
            data = callAPI(url)
            for i in data["items"]: 
                element = getData(i)
                transactions.append(element)
            if data["next_page_path"]:
                url = "https://explorer.3achain.org"+data["next_page_path"]+"&type=JSON"
                currentBlock = data["next_page_path"].split("?")[1].split("&")[0].split("=")[1]

            with open(TEMP, "a+") as f:
                for t in transactions:
                    json.dump(t, f)
                    f.write("\n")

            print(f"Request number: {done} | Current block: {currentBlock}")
            if not data["next_page_path"] or int(currentBlock) < int(lastblock):
                break
        
            sleep(SLEEPTIME)
            transactions = []
            done += 1
        except KeyboardInterrupt:
            break
    
    # Once it's done, open the temp file, flip the data and append to the end of the other list
    convertToMain()

    # remove duplicates
    removeDuplicate()

    # finally delete the temp file
    os.remove(TEMP)

    
        


if __name__ == "__main__":
    #convertToMain()
    download()