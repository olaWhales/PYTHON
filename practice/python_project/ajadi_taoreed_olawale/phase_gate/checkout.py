user = true;
sum = 0;
item = "";
quantity = 0;
price = 0;
discounts = 0;
discount = 0;
discountgiven ;

print("whats the customer's Names: ")

		
print("==============================================================")
print("%s\n%s\n%s\n%s\n%s","SEMICOLON", "MAIN BRANCH", "LOCATION: 312, HERBERT MACAULEY WAY, SABO YABA, LAGOS.","TEL: 08102790000","Cashier: Cashier's Name")
print("Date: " + todaysDate)
print("Customer Name: " + customerName )
print("==============================================================")
print("		ITEM	QTY	PRICE	TOTAL(NGN)")
print("--------------------------------------------------------------")
print("		%4s%6d%9d%9d",item, quantity, price, sum)
print()
print("--------------------------------------------------------------")
print("		%s%4d\n		%s%4f", "Sub Total:	", sum, "Discount:	", discountgiven )
print()
print("==============================================================")
print("		%4s%9d", "Bill Total",sum)
print()
print("==============================================================")
print("%s%4d", "THIS IS NOT A RECEIPT KINDLY PAY:  ", sum )
print()
print("==============================================================")

	
print("How much did the user gave to you? ")
paid = input.nextInt()
amountPaid = paid - sum


print("%s\n%s\n%s\n%s\n%s","SEMICOLON", "MAIN BRANCH", "LOCATION: 312, HERBERT MACAULEY WAY, SABO YABA, LAGOS.","TEL: 08102790000","Cashier: Cashier's Name")
print()
print("Date: " + todaysDate)
print("Customer Name: " + customerName )
print("==============================================================")
print("		ITEM	QTY	PRICE	TOTAL(NGN)")
print("--------------------------------------------------------------")
print("		%4s%6d%9d%9d",item, quantity, price, sum)
print()
print("--------------------------------------------------------------")
print("		%s%4d\n		%s%4f", "Sub Total:	", sum, "Discount:	", discountgiven )
print()
print("==============================================================")
print("		%4s%9d\n		%4s%9d\n		%4s%9d", "Bill Total:", sum, "Amount Paid:", paid, "Balance:", amountPaid)
print()
print("==============================================================")
print("THANK YOU FOR YOUR PATRONAGE")
print("==============================================================")
