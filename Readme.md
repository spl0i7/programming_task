# Stock analysis helper


## Install
- This program uses fuzzywuzzy package for fuzzy string matching.
- Install dependencies `pip3 install -r requirements.txt`.

## Run
- `python3 main.py dataset.csv`

## Sample Outputs
```bash

Enter Stock : aix
Did you mean AICIXE? (y/n)y
Enter Start Date : 23-jan-2018
Enter End Date : 20-jan-2020
Mean : 20.7265
Std : 0.38678740930904193

Buy at : 20-Jan-2019
Sell at : 21-Jan-2019
Profit(per Stock) = 0.5470000000000006

Do you want to continue ? (y/n)y
Enter Stock : aix
Did you mean AICIXE? (y/n)y
Enter Start Date : 
Did not recognize format, going to earliest
Enter End Date : 
Did not recognize format, going to farthest
Mean : 20.7265
Std : 0.38678740930904193

Buy at : 20-Jan-2019
Sell at : 21-Jan-2019
Profit(per Stock) = 0.5470000000000006

Enter Stock : am
Did you mean AMBKP? (y/n)y
Enter Start Date : 22-jan-2019
Enter End Date : 26-jan-2019
Mean : 32.387
Std : 4.335978782235911

Buy at : 22-Jan-2019
Sell at : 23-Jan-2019
Profit(per Stock) = 6.1320000000000014

Do you want to continue ? (y/n)y
Enter Stock : asd
Did you mean AICIXE? (y/n)n
Enter Stock : 

```