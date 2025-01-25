def money_count(n, coins):
    if len(coins) == 1:
        if n % coins[0] == 0:
            return 1
        return 0  
    
    res = 0
    for i in range(n // coins[0] + 1):
        left = n - coins[0] * i
        if left == 0:
            res += 1
            break
        res += money_count(left, coins[1:])

    return res 
        
def money_count_print(n, coins, dic={}):
    if len(coins) == 1:
        if n % coins[0] == 0:
            print(dic | {coins[0]: n // coins[0]})
            return 1
        return 0  
    
    res = 0
    for i in range(n // coins[0] + 1):
        left = n - coins[0] * i
        if left == 0:
            print(dic | {coins[0]: i})
            res += 1
            break
        res += money_count_print(left, coins[1:], dic | ({coins[0]: i} if i != 0 else {}))
        
    return res

currencies = [1, 2, 5, 10, 20, 50, 100, 200]
currencies.sort(reverse=True)
print(money_count_print(200, currencies))