import math


def optimal_change(item_cost, amount_paid):
    change = round(amount_paid - item_cost, 2)
    result = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
    result_without_and = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
    residual = 0
    ls_of_amount = []
    # while round(change, 10) != 0.0:
    # $100
    if change >= 100:
        residual = math.floor(change/100)
        change -= residual * 100
        amount_money = f"{residual} $100 bill"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $50
    if change >= 50:
        residual = math.floor(change/50)
        change -= residual * 50
        amount_money = f"{residual} $50 bill"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $20
    if change >= 20:
        residual = math.floor(change/20)
        change -= residual * 20
        amount_money = f"{residual} $20 bill"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $10
    if change >= 10:
        residual = math.floor(change/10)
        change -= residual * 10
        amount_money = f"{residual} $10 bill"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $5
    if change >= 5:
        residual = math.floor(change/5)
        change -= residual * 5
        amount_money = f"{residual} $5 bill"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $1
    if change >= 1:
        residual = math.floor(change/1)
        change -= residual * 1
        amount_money = f"{residual} $1 bill"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $0.25
    if change >= 0.25:
        residual = math.floor(change/0.25)
        change -= residual * 0.25
        amount_money = f"{residual} quarter"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $0.1
    if change >= 0.1:
        residual = math.floor(change/0.1)
        change -= (residual * 0.1)
        amount_money = f"{residual} dime"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
        # $0.05
    if change >= 0.05:
        residual = math.floor(change/0.05)
        change -= residual * 0.05
        amount_money = f"{residual} nickel"
        ls_of_amount.append(amount_money)
        result += amount_print(change, residual, amount_money)
    # $0.01
    else:
        residual = round(change * 100)
        change -= residual * 0.01
        amount_money = f"{residual} penn"
        ls_of_amount.append(amount_money)
        result += penny_print(residual, amount_money)
        
    # in case of there is no 'and'
    if len(ls_of_amount) == 1:
        if "penn" in ls_of_amount[0]:
            if residual != 1:
                result_without_and += ls_of_amount[0] + "ies."
            else:
                result_without_and += ls_of_amount[0] + "y."
        else:
            if residual != 1:
                result_without_and += ls_of_amount[0] + "s."
            else:
                result_without_and += ls_of_amount[0] + "."
        return result_without_and
            
    return result

def amount_print(change, residual, amount_money):

    # this condition is to figure out if it is plural
    if residual != 1:
        amount_money += "s"
    
    # this codition is to figure out if it is end of the sentence or not
    if change == 0.0:
        amount_money = "and " + amount_money + "."
    else:
        amount_money += ", "

    return amount_money

# this method helps to print $100, $50, $20, $10, $5, $1
def penny_print(residual, amount_money):
    result = f"and {amount_money}"

    # this condition is to figure out if it is plural
    if residual != 1:
        result += "ies."
    else:
        result += "y."

    return result

