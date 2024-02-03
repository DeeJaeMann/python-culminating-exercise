#!/usr/bin/env python3.12
def exact_change(item_cost, money_paid):


    dct_currency = {
        "One Hundred" : 100,
        "Fifty" : 50,
        "Twenty" : 20,
        "Ten" : 10,
        "Five" : 5,
        "Two" : 2,
        "One" : 1,
        "Quarter" : 0.5,
        "Dime" : 0.1,
        "Nickle" : 0.05,
        "Penny" : 0.01,
    }

    if item_cost <= money_paid :
    
        # Calculate the final total
        flt_total = money_paid - item_cost
        str_response = f"Your total is {flt_total:.2f}"

        if flt_total > 0 :
            # Set the temp change to total.  This var is used to calculate the exact change
            flt_temp_change = flt_total

            while flt_temp_change > 0 :
                pass
        else :
            str_response += "."

        return str_response
    else :
        return "You can't afford this item." 

#print(exact_change(53.73, 100))
#print(exact_change(10.0, 3.00))
print(exact_change(10, 10))
