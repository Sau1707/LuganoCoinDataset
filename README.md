## LVGA POINT DATASET

This folder create an algorithm to scrape data from:
https://explorer.3achain.org/token/0x1cC4967fF6592E6672827809767dF82A49f7c30D

#### Data

The data is set into `/data` and it's saved in json syntax.
This is a example of a value in the dataset

```json
{
	"block": "4101482", // block number
	"time": "2022-06-21 13:13:44.000000Z", // time of transaction
	"quantity": "400", // LVGA coin tranfered
	"sender": "0x3BB4294684ef91d934b7B2aD0d8Ae09812Ae188A", // sender wallet
	"reciver": "0xF96a9f4829dBA08b7ECcb79da8B4868e5D2DFFa3" // sender reciver
}
```

#### Update the dataset

To update the dataset:

```bash
cd src
python main.py
```

it automatically download the new data and update the last inside data folder, as well year and month if have changed.

#### Disclaimer

This project can create a lot of traffic at https://explorer.3achain.org/

Use wisely
