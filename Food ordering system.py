
total = 0
A = ["DABELI", float(2.50), 50],["VADAPAV", float(0.50), 200],["DOSA", float(1.00), 20],["PUF", float(2.50), 44],["GOTA", float(0.50), 35],["VADA", float(1.00), 20],["SAMOSA", float(2.50), 90],["IDLI", float(0.50), 60],["BURGER", float(1.00), 100]

def processOrder(quantity, item_list):
    global total
    if quantity > item_list[2]:
        print("There is not enough stock!")
        pass
    else:
        total += item_list[1] * quantity
        print(total)
        item_list[2] -= quantity


print("Welcome to Foodela")
print("[1]", A[0][0:3],
      "\n[2]", A[1][0:3],
      "\n[3]", A[2][0:3],
      "\n[4]", A[3][0:3],
      "\n[5]", A[4][0:3],
      "\n[6]", A[5][0:3],
      "\n[7]", A[6][0:3],
      "\n[8]", A[7][0:3],
      "\n[9]", A[8][0:3])

while True:
    choice, quantity = (input("\nWhat would you like?\n")).upper(), int(input("\nHow many would you like?\n"))

    if choice == "DABELI" or choice=="1":
        processOrder(quantity, A[0])
    elif choice == "VADAPAV" or choice=="2":
        processOrder(quantity, A[1])
    elif choice == "DOSA" or choice== "3":
        processOrder(quantity, A[2])
    elif choice == "PUF" or choice== "4":
        processOrder(quantity, A[3])
    elif choice == "GOTA" or choice=="5":
        processOrder(quantity, A[4])
    elif choice == "VADA" or choice=="6":
        processOrder(quantity, A[5])
    elif choice == "SAMOSA" or choice=="7":
        processOrder(quantity, A[6])
    elif choice == "IDLI" or choice=="8":
        processOrder(quantity, A[7])
    elif choice == "BURGER" or choice=="9":
        processOrder(quantity, A[8])
    else:
        print("Invalid Item")

    more_items = (input("Do you want to order more items?""\n Type 'Y' for Yes and 'N' for No")).upper()
    if more_items == "Y":
        pass
    elif more_items == "N":
        print("Here is the total amount you will be charged"
              "\n\t\t\t", str(total))
        confirm =(input("\n Do you want to place this order?")).upper()
        if confirm== "Y":
            break
    else:
        break

print("Thank you for ordering!\nYour total cost is: £", str(total))

