"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

if sales < 0:
    print("invalid number")
elif sales >= 1000:
    fifteen_per = (sales * 0.15)
    print("${:d}".format(int(fifteen_per)))
elif sales < 1000:
    ten_per = (sales * 0.1)
    print("${:d}".format(int(ten_per)))
