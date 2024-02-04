#!/usr/bin/env python3.12
import re

def check_dollars(flt_value) :
    # If our value is greater than 1 then we have append 'Dollar Bill'
    if flt_value >= 1 :
        return " Dollar Bill"
        
    return ""

def check_penny(int_divisor) :
    # Check if we have multiple pennies
    if int_divisor > 1:
        return "ies"
    
    # We have one penny
    return "y"

def parse_spaces(str_raw) :
    # This pattern uses positive look arounds to locate a letter with
    # a number directly after.
    # Lookarounds do not consume the match so this enables us to insert
    # using RegEx
    regex_raw_line = re.compile(r'(?<=[lser])(?=\d)', re.I)

    if regex_raw_line.search(str_raw) :
        # we found a match so we'll insert a comma and a space.
        return re.sub(regex_raw_line, ", ", str_raw)

    return str_raw



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
                    # This unit is divisible

                    # Add the divisible amount (count of units) and unit name
                    str_response += f"{int_tmp_divide} {str_key}"
                    flt_tmp_change -= flt_value * int_tmp_divide

                    # Ensure we round up to two decimal places
                    flt_tmp_change = round(flt_tmp_change, 2)

                    str_response += f"{check_dollars(flt_value)}"

                    if(flt_value == .01) :
                        # We have pennies, append whether we're plural or singular
                        str_response += f"{check_penny(int_tmp_divide)}"
                    elif(int_tmp_divide > 1) :
                        # We have multiple others, make it plural
                        str_response += "s"

        str_response += "."

        str_response = parse_spaces(str_response)

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
print(exact_change(0.75, 5))
print(exact_change(1.34, 5))
print(exact_change(1.34, 1.36))
#print(exact_change(9.99, 20))