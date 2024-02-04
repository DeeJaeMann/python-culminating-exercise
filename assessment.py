#!/usr/bin/env python3.12
import re
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

                    flt_tmp_change = round(flt_tmp_change, 2)
                    
                    # print(f"**1**Evaluating {str_key} Tmp Change {flt_tmp_change} Divide {int_tmp_divide}")
                    # print(f"**2**{str_response}")

                    if flt_value >= 1 :
                        str_response += " Dollar Bill"

                    # Check if we have multiple coins
                    #   and check if we have a penny
                    if int_tmp_divide > 1 and flt_value > .01 :
                        str_response += "s"
                    elif int_tmp_divide > 1 and flt_value == .01:
                        # We have pennies, pluralize the response
                        str_response += "ies"
                    elif flt_value == .01 :
                        # We have one penny
                        str_response += "y"

                    # If we have more change to calculate add a comma
                    if flt_tmp_change > 0.01 :
                        str_response += ", "


        #else :
        str_response += "."

        regex_final_comma_pattern = re.compile(r", (\d+ \w+.)$")
        if regex_final_comma_pattern.search(str_response) :
            #print("Matched!")
            str_response = re.sub(r", (\d+ \w+.)$", r", and \1", str_response)

        # Check for single dollar bill
        regex_single_dollar_pattern = re.compile(r": (\d+ \w+ \w+ \w+), and (\d+ \w+.)$")
        if regex_single_dollar_pattern.search(str_response) :
            #print("Matched!")
            str_response = re.sub(regex_single_dollar_pattern, r": \1 and \2", str_response)

        return str_response
    else :
        return "You can't afford this item." 

#print(exact_change(53.73, 100))
#print(exact_change(10.0, 3.00))
#print(exact_change(0.75, 2))
print(exact_change(1.34, 5))
#print(exact_change(9.99, 20))