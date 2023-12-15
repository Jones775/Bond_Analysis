from collections import OrderedDict
import random

def primary_auction(buy_orders, sell_orders):
    #The Parameter are both dictionaries that contain all prices and the amount of Orders for that price

    buy_orders = OrderedDict(buy_orders)
    sell_orders = OrderedDict(sell_orders)

    possible_trades = {}

    #Number of Bonds that would be buyed at a certain price
    possible_buys = OrderedDict()
    #Number of Bonds that would be sold at a certain price
    possible_sells = OrderedDict()

    #Create Dictionary with all prices and the amount of Bonds that would be buyed at this price
    buys = 0
    for element in reversed(buy_orders):
        buys += buy_orders[element]
        possible_buys[element] = buys

    #Create Dictionary with all prices and the amount of Bonds that would be sold at this price
    sells = 0
    for element in sell_orders:
        sells += sell_orders[element]
        possible_sells[element] = sells

    #Calculate how many Bonds would be traded at a certain price
    for element in possible_buys:
        buys = possible_buys[element]
        sells = possible_sells[element]

        if buys > sells:
            possible_trades[element] = sells
        elif sells > buys:
            possible_trades[element] = buys
        elif sells == buys:
            possible_trades[element] = buys


    #Get Price at which most Bonds are traded
    max_value = 0
    max = 0
    for element in possible_trades:
        if int(possible_trades[element]) > max_value:
            max = element
            max_value = possible_trades[element]

    #Return the price at which most Bonds are traded
    return max





def secondary_auction(last_price, buy_orders, sell_orders):
    #The parameters are arrays, with all prices there are orders for
    buy_orders.sort(reverse=True)
    sell_orders.sort()
    price = last_price


    buy_order = buy_orders[0]
    sell_order = sell_orders[0]
    if buy_order < sell_order:
        return None, buy_orders, sell_orders
    elif buy_order > sell_order:
        price = round((buy_order+sell_order)/2)
        buy_orders.pop(0)
        sell_orders.pop(0)
        return price, buy_orders, sell_orders
    elif buy_order == sell_order:
        price = sell_order
        buy_orders.pop(0)
        sell_orders.pop(0)
        return price, buy_orders, sell_orders




buy_orders = {20: 1000, 21:700, 22: 500, 23: 300, 24: 100}
sell_orders = {20: 200, 21: 300, 22: 590, 23: 800, 24: 1000}

price = primary_auction(buy_orders, sell_orders)
print(price)

buy_orders = [20, 22, 21, 18, 17, 25]
sell_orders = [21, 25, 22, 22, 24, 27]


while price != None:
    print(price)
    price, buy_orders, sell_orders = secondary_auction(price, buy_orders, sell_orders)
    sell_orders.append(random.randint(0,50))
    buy_orders.append(random.randint(0,50))
