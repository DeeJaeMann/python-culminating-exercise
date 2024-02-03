#!/usr/bin/env python3.12
def exact_change(item_cost, money_paid):
    str_response = "Your total is "

    dct_currency = {
        "One Hundred Dollar Bill" : 100,
        "Fifty Dollar Bill" : 50,
        "Twenty Dollar Bill" : 20,
        "Ten Dollar Bill" : 10,
        "Five Dollar Bill" : 5,
        "Two Dollar Bill" : 2,
        "One Dollar Bill" : 1,
        "Quarter" : 0.5,
        "Dime" : 0.1,
        "Nickle" : 0.05,
        "Penny" : 0.01,
    }

    if item_cost < money_paid :
        return f"{str_response} {dct_currency}"
    else :
        return "You can't afford this item." 

#print(exact_change(53.73, 100))
print(exact_change(10.0, 3.00))
