import random
import time

def draw_Chart(price, last_price, timepoint, last_prices):
    #Draws Chart of the Bond in ASCII-Style

    #Clear last chart
    for _ in range(200):
        print()

    print("  ^")
    for counter in range(99):
        num = 99-counter
        
        print("{0:02}".format(num), end="")

        #Checking if Bond had this price in the past
        times_bond_had_same_price = []
        for counter in range(len(last_prices)-1):
            if last_prices[counter] == price:
                times_bond_had_same_price.append(counter)
        times_bond_had_same_price.append(num)


        #This will be executed if somewhere in the past, the price of the Bond was at this price
        if len(times_bond_had_same_price) != 0:
            print("|", end = "")


            last_time = 0
            for element in times_bond_had_same_price:
                for _ in range(element-last_time-1):
                    print(" ", end="")
                if times_bond_had_same_price.index(element) == len(times_bond_had_same_price)-1:
                    print("*", end="")
                else:
                    print("*", end="")
                last_time = element
            print("*")

        #This will be executed if nowhere in the past the price of the bond was at this price
        else:
            print("|")
    print("  *------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>")



price = 10
last_prices = []
for timepoint in range(100):
    last_price = price
    last_prices.append(last_price)
    price = price + random.randint(-1, 1)
    draw_Chart(price, last_price, timepoint, last_prices)
    time.sleep(0.25)
