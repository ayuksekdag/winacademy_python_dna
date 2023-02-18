# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

#part 1
leek_price = 2
print(f"Leek is " + str(leek_price) + " euro per kilo.")

#part 2
leek_order = "leek 4"
leek_amount = int(leek_order[5])
sum_total = leek_amount * leek_price
print(sum_total)

#part3

brocoli_order = 'broccoli 1.6'
brocoli_price = 2.34
brocoli_order_amount = brocoli_price * float(brocoli_order[9:])
print('1.6kg broccoli costs ' + str(round(brocoli_order_amount, 2)) + "e")
