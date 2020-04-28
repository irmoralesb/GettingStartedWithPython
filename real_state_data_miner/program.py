import csv
import os
from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print("------------------------------------")
    print("      REAL STATE DATA MINER")
    print("------------------------------------")


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, "data", "SacramentoRealEstateTransactions2008.csv")


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            # print("Bed count: {}".format(row["beds"]))
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        # This way you need to use numeric indexes!
        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(type(row), row)
        #     beds = row[4]
        return purchases


def get_price(p):
    return p.price


def query_data(data):
    # Sort way 1
    # data.sort(key=get_price)

    # sort way 2
    data.sort(key=lambda p: p.price)
    # most expensive house?
    high_purchase = data[-1]
    print("The most expensive house is ${:,}".format(data[-1].price))
    # least expensive house?
    low_purchase = data[0]
    print("The least expensive house is ${:,}".format(data[0].price))
    # average price house
    # average price of 2 bedroom house?


if __name__ == "__main__":
    main()
