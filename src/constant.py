# Last block, the contract has been created this block
BLOCKLIMIT = 4029
# Set a hight stat block that the network will never reach as first request.
STARTBLOCK = 9999999
# Name of the file containg all the data
FILENAME = "all.csv"
TEMP = "temp.csv"
# Start url, parsed with the stating block
STARTURL = f"https://explorer.3achain.org/token/0x1cC4967fF6592E6672827809767dF82A49f7c30D/token-transfers?block_number={STARTBLOCK}&index=0&items_count=50&type=JSON"
# Define deta time between each request
SLEEPTIME = 0.1