import csv
import os
import statistics

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
    # USING List Comprehensions
    prices = [
        p.price  # projection or items
        for p in data  # The set to process
    ]
    mean_price = statistics.mean(prices)
    print("The average house price is ${:,}".format(int(mean_price)))
    # average price of 2 bedroom house?
    two_bed_homes = [
        p
        for p in data
        if p.beds == 2
    ]
    # List comprehensions
    ave_price = statistics.mean([p.price for p in two_bed_homes])
    ave_baths = statistics.mean([p.baths for p in two_bed_homes])
    ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print(
        "The average 2 bedrooms house price is ${:,}, baths={}, sq_ft={:,}".format(int(ave_price), round(ave_baths, 1),

                                                                                   round(ave_sqft, 1)))

    # Same sample but using Generator Expression
    # ONE ITEM PROCESSED AT A TIME
    two_bed_homes = (
        p
        for p in data
        if p.beds == 2
    )
    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, "price") for p in homes))
    ave_baths = statistics.mean((announce(p.baths, "baths") for p in homes))
    ave_sqft = statistics.mean((announce(p.sq__ft, "square feet") for p in homes))
    print(
        "The average 2 bedrooms house price is ${:,}, baths={}, sq_ft={:,}".format(int(ave_price), round(ave_baths, 1),

                                                                                   round(ave_sqft, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == "__main__":
    main()
