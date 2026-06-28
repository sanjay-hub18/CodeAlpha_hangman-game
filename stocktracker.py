stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3500,
    "MSFT": 300
}

# Dictionary to store user's stock and quantity
user_portfolio = {}

# Get user input
print("Enter stock details (type 'done' to finish):")
while True:
    stock_name = input("Stock Symbol (e.g., AAPL): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print("Stock not in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
        user_portfolio[stock_name] = user_portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
result_lines = ["Your Investment Summary:\n"]
for stock, qty in user_portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    result_lines.append(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

result_lines.append(f"\nTotal Investment: ${total_investment}")

# Display result
print("\n".join(result_lines))

# Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    with open("investment_summary.txt", "w") as file:
        file.write("\n".join(result_lines))
    print("Summary saved to 'investment_summary.txt'")
