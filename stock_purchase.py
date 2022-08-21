# Aeriel Denmark
# Stock Purchase

import math

# This program will create a function that outlines the parameters of purchasing stocks based on 
# an individual's earnings and desired contribution

def stock_purchase():
	print("Welcome to the stock purchase program! \nYou may contribute 1%-10% of your total earnings to stock purchases.\n"
	        "You will receive 15% off of the lowest stock purchase price.\n")
	
	earnings = int(input("Enter your total earnings: "))
	contribution = int(input("Enter desired contribution percentage: "))
	amount = ((earnings) * (contribution / 100))
	print("You may use $", "{:.2f}".format(amount), "towards your stock purchase based on your earnings",
	                        "and desired contribution.")
	start = float(input("\nEnter starting stock price: "))
	end = float(input("Enter ending stock price: "))
	
	if start > end:
	    final_stock_price = end
	    print("\nYou will receive 15% off of the ending stock price of $", "{:.2f}".format(end))
	    print("Your stock purchase price will be $","{:.2f}".format(end * 0.85))
	elif start < end:
	    final_stock_price = start
	    print("\nYou will receive 15% off of the starting stock price of $", "{:.2f}".format(start))
	    print("Your stock purchase price will be $","{:.2f}".format(start * 0.85))
	else:
	    final_stock_price = start
	    print("\nThe starting and ending stock prices are the same.  You will receive 15% off of either stock price.")
	    print("Your stock purchase price will be $","{:.2f}".format(start))
	    
	print("\nBased on your earnings, your desired contribution, and your stock purchase price, "
	        "you will be able to purchase","{:.2f}".format(amount / final_stock_price), "stock(s).")
		
stock_purchase()



