# given a set of coin denominations and a target amount, find the minimum number of coins needed to 
# make up that amount.

coins = [1, 5, 10, 25]  # Denominations of coins (in cents)
amount = 99
def coin_change(coins, amount):
    coins.sort(reverse=True)
    num_coins=0
    i=0
    while amount>0 and i<len(coins):
        if coins[i]<=amount:
            num_coins+=amount//coins[i]
            amount=amount%coins[i]
        i+=1
    return num_coins

print(f"The number of coins needed to make up {amount} shillings is {coin_change(coins, amount)}")

