prices = [7, 1, 5, 3, 6, 4,]
lowest = prices[0]      
profit = 0

for i in range(1, len(prices)):
    if prices[i] < lowest:
        lowest = prices[i]

    current_profit = prices[i] - lowest

    if current_profit > profit:
        profit = current_profit

print(profit)