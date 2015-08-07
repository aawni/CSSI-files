sales_tax= .09
prices= {"water":1, "kumquat":4.50,"apple":.75}

def compute_tax(subtotal):
    return sales_tax*subtotal

def calculate_final_price(item_value):
    return item_value + compute_tax(item_value)

def calculate_final_price_by_name(item_name):
    if 
    return calculate_final_price(prices[item_name])



print ('Please insert item name')
user_input = raw_input()
if
print calculate_final_price_by_name(user_input)
