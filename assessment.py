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
        "Quarter" : 0.25,
        "Dime" : 0.1,
        "Nickle" : 0.05,
        "Penn" : 0.01,      # Penny
    }

    if item_cost <= money_paid :
    
        # Calculate the final total
        flt_total = money_paid - item_cost
        str_response = f"Your total is {flt_total:.2f}"

        if flt_total > 0 :
            # Set the temp change to total.  This var is used to calculate the exact change
            flt_tmp_change = flt_total

            # Add the colon and space
            str_response += ": "

            # Iterate through our currency dict and determine our change
            for str_key, flt_value in dct_currency.items() :
                # Type Cast to int so that we're not dealing with decimals
                int_tmp_divide = int(flt_tmp_change // flt_value)
                # Check if this coin is divisible
                if int_tmp_divide > 0 :
                    str_response += f"{int_tmp_divide} {str_key}"
                    flt_tmp_change -= flt_value * int_tmp_divide
                    
                    # Check if we have multiple coins
                    #   and check if we have a penny
                    if int_tmp_divide > 1 and flt_value > .01 :
                        str_response += "s "
                    elif int_tmp_divide > 1 and flt_value == .01:
                        str_response += "ies"


        else :
            str_response += "."

        return str_response
    else :
        return "You can't afford this item." 

#print(exact_change(53.73, 100))
#print(exact_change(10.0, 3.00))
#print(exact_change(10, 10))
print(exact_change(50.73, 51.25))