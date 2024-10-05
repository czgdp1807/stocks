import argparse
import json
import math
import csv

PE_THRESHOLD = 35
PB_THRESHOLD = 3

def compute_stock_weight(pe, pb, stock):
    if pe < PE_THRESHOLD and pb < PB_THRESHOLD:
        stock["weight"] = 2.5
    elif pe > PE_THRESHOLD and pb > PB_THRESHOLD:
        stock["weight"] = 0.5
    else:
        stock["weight"] = 1.5
    return stock["weight"]

def compute_weights(portfolio):
    for stock in portfolio:
        pe = stock["pe"]
        pb = stock["pb"]
        weight = compute_stock_weight(pe, pb, stock)

def sum_weights(portfolio):
    total = 0
    for stock in portfolio:
        total += stock["weight"]
    return total

def compute_portfolio(path, target_amount):
    portfolio = {}
    with open(path) as f:
        portfolio = json.load(f)

    compute_weights(portfolio)
    total = sum_weights(portfolio)
    target_amount_per_unit_weight = target_amount/total

    for stock in portfolio:
        current_market_value = stock["market_value"]
        stock["market_value"] = target_amount_per_unit_weight * stock["weight"]
        stock["shares (buy/sell)"] = math.ceil((stock["market_value"] - current_market_value)/stock["price"])
        stock["amount_needed"] = stock["shares (buy/sell)"] * stock["price"]
        stock["shares"] += stock["shares (buy/sell)"]
        stock["market_value"] = abs(stock["price"] * stock["shares"])
        stock["previous_market_value"] = current_market_value

    return portfolio

def tabulate_portfolio(portfolio):
    with open('portfolio.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=portfolio[0].keys())
        writer.writeheader()
        writer.writerows(portfolio)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse information needed for portfolio calculation.')
    parser.add_argument('--path', dest='path', required=True)
    parser.add_argument('--target-amount', dest='target_amount', required=True, type=float)

    args = parser.parse_args()
    portfolio = compute_portfolio(args.path, args.target_amount)
    tabulate_portfolio(portfolio)
