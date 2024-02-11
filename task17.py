from datetime import datetime
name = input("ENTER YOUR NAME: ")
lists = """
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     RS 80/litre
Colgate Rs 10/each

"""

# declaration
price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []
# rates for items
items = {
    "rice": 20,
    "sugar": 30,
    "salt": 20,
    "oil": 80,
    "colgate": 10
}

option = int(input("for list of items press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("for buying press 1 and 2 for exit"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("enter your items: ")
        quantity = int(input("enter your qty: "))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item, quantity, items, price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalamount = gst+totalprice
        else:
            print("your entered items is not available")
    else:
        print("you entered wrong number: ")
    inp = input("can i bill the items yes or no")
    if inp == "yes":
        pass
        if finalamount != 0:
            print(25*"=", "vasu supermarket", 25*"=")
            print(28*" ", "tadepalligudem")
            print("Name:", name, 30*" ", "Fate:", datetime.now())
            print(75*"_")
            print("Sno,", 8*" ", "item", 8*" ", "Qty", 3*" ", "price")
            for i in range(len(pricelist)):
                print(i, 8*" ", 8*" ", ilist[i], 3*" ", qlist[i], plist[i])
            print(75*"-")
            print(50*" ", "total:", "Rs", totalprice)
            print("gst amount", 50*" ", "Rs", gst)
            print(75*"-")
            print(50*" ", "finalamount: ", "Rs", finalamount)
            print(75*"-")
            print(50*" ", "Thanks for visiting")
            print(75*"-")
