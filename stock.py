import datetime
import statistics

class Stock:
    def __init__(self, stockname):
        self.stockname = stockname
        self.data = list()

    def add_record(self, date_str, price):
        date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
        self.data.append((date, float(price)))

    def get_buy_sell_information(self, start=None, end=None):

        self.sort_by_time()
        prices = self.get_prices_range(start, end, date=True)

        max_profit = 0
        buy_date = None
        sell_date = None

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j][1] - prices[i][1] > max_profit:
                    buy_date = prices[i][0]
                    sell_date = prices[j][0]
                    max_profit = prices[j][1] - prices[i][1]

        return buy_date, sell_date, max_profit

    def sort_by_time(self):
        self.data.sort(key= lambda x : x[0])

    def get_prices(self):
        return list(map(lambda x : x[1], self.data))

    def get_prices_range(self, start=None, end=None, date=False):
        if start is None:
            start = datetime.datetime.strptime('01-Jan-1900', '%d-%b-%Y')
        if end is None:
            end = datetime.datetime.strptime('31-Dec-2500', '%d-%b-%Y')

        ranged_prices = []
        for i in self.data:
            if start <= i[0] <= end:
                if not date:
                    ranged_prices.append(i[1])
                else: ranged_prices.append(i)
        return ranged_prices

    def calculate_mean(self, start=None, end=None):
        prices = self.get_prices_range(start, end)
        if len(prices) < 1: return None
        return statistics.mean(self.get_prices_range(start, end))

    def calculate_std(self, start=None, end=None):
        prices = self.get_prices_range(start, end)
        if len(prices) <= 1: return 0
        return statistics.stdev(prices)

    def __repr__(self):
        representation = str()
        for d in self.data:
            representation += "{} {}\n".format(d[0], d[1])
        return representation

