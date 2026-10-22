

try:
    weight = float(input("Weight kg: "))

except ValueError:
    
    print("Please enter a valid weight")
else:
    if weight <= 0:
        print("Please enter a valid weight")
    
    elif weight > 20:
        print("Too heavy(max 20 kg)")
    
    else:
        destination = input("Destination (bangkok/other): ")
    
        if destination != "bangkok" and destination != "other":
            print("Unknown destination")
    
        else:
            express = input("Express? (yes/no): ")

            if weight <= 1:
                cost = 40
            elif weight <= 5:
                cost = 80
            else:
                cost = 150

            if destination == "other":
                OUTSIDE_FEE = 30
                cost = cost + OUTSIDE_FEE

            if express == "yes":
                cost = cost * 2

            print("Shipping cost:", cost, "baht")
