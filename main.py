import csv
import sys
import datetime
from fuzzywuzzy import process

from stock import Stock

def read_csv_data(filename):
    raw_data = list()
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for row in reader:
                raw_data.append(row)
    except Exception as e:
        print(e)

    return raw_data

def parse_csv_file(raw_data_list):
    data_dict = dict()
    for row in raw_data_list:
        if row[0] not in data_dict:
            data_dict[row[0]] = Stock(row[0])

        data_dict[row[0]].add_record(row[1], row[2])

    for v in data_dict.values() : v.sort_by_time()

    return data_dict

def print_analysis(stock, start, end):
    mean = stock.calculate_mean(start, end)
    std_dev = stock.calculate_std(start, end)
    buy, sell, profit = stock.get_buy_sell_information(start, end)

    if mean is None:
        print("No datapoints found for this range")
        return

    print("Mean : {}\nStd : {}\n".format(mean, std_dev))

    if buy is not None :
        print("Buy at : {}\nSell at : {}\nProfit(per Stock) = {}\n".format(buy.strftime('%d-%b-%Y'), sell.strftime('%d-%b-%Y'), profit))
    else :
        print("No profitable period found")

def string_lookup(typo_string, string_list):
    searches = process.extract(typo_string, string_list, limit=1)
    if len (searches ) > 0:
        return searches[0][0]
    else: return ""


def main(filename):
    raw_data_list = read_csv_data(filename)
    if len(raw_data_list) == 0:
        print("No records found")
        sys.exit(-1)
        
    records = parse_csv_file(raw_data_list)

    while True:
        stock_name = input("Enter Stock : ")
        try:
            stock = records[stock_name]
        except KeyError as e:
            fuzzy_key = string_lookup(stock_name, records.keys())
            if len(fuzzy_key) > 0 :
                yes_no = input("Did you mean {}? (y/n)".format(fuzzy_key))
                if yes_no == "y" :
                    stock = records[fuzzy_key]
                else : continue




        start = input("Enter Start Date : ")

        try:
            parsed_start = datetime.datetime.strptime(start, '%d-%b-%Y')
        except:
            print("Did not recognize format, going to earliest")
            parsed_start = None



        end = input("Enter End Date : ")
        try:
            parsed_end =  datetime.datetime.strptime(end, '%d-%b-%Y')
        except:
            print("Did not recognize format, going to farthest")
            parsed_end = None

        print_analysis(stock, parsed_start, parsed_end)

        yes_no = input("Do you want to continue ? (y/n)")
        if yes_no == "n": break



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : {} <Path-To-Csv>".format(sys.argv[0]))
    else:
        main(sys.argv[1])
