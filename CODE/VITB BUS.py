import datetime   

print("Current date and time:")
print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

seats = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28]
]

def showSeats():
    print("\nSeat Layout (XX = booked):")
    for row in seats:
        for s in row:
            if s == 0:
                print("XX", end="  ")
            else:
                print(f"{s:02}", end="  ")  
        print()


def bookSeat(bus_name):
    while True:
        print(f"\nBooking seat for: {bus_name}")
        showSeats()

        try:
            choice = int(input("\nEnter seat number to book (0 to go back) = "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if choice == 0:
            print("Returning to main menu...")
            return  # seedha MENU pe wapas

        if choice < 1 or choice > 28:
            print("❌ Invalid seat number! (1–28 allowed)")
            continue

        
        found_free = False
        for i in range(len(seats)):        
            for j in range(len(seats[0])): 
                if seats[i][j] == choice:  
                    seats[i][j] = 0       
                    print(f"✅ Seat {choice} booked successfully!")
        
                    return
        
        print("❌ Seat already booked! Please choose another seat.")

def Ticketbooking():

    print("\nPlease choose where you would like to travel")
    print("1: VIT To Bhopal")
    print("2: VIT To Ashta")
    print("3: VIT To Sehore")
    route = int(input("Please tell us your destination (1,2,3) = "))

    
    if route == 1:
        print("\nAvailable buses for your given date and destination are listed below:")

        buses = [
            "VIT TO BHOPAL | Bus Number:1212 | Time: 4:00P.M.",
            "VIT TO BHOPAL | Bus Number:1214 | Time: 4:30P.M.",
            "VIT TO BHOPAL | Bus Number:1215 | Time: 5:00P.M.",
            "VIT TO BHOPAL | Bus Number:1216 | Time: 5:30P.M.",
            "VIT TO BHOPAL | Bus Number:1219 | Time: 6:30P.M."
        ]

        for i, b in enumerate(buses, start=1):
            print(f"{i}: {b}")

        bus = int(input("Please choose the bus you would like to travel in (1-5) = "))

        if 1 <= bus <= 5:
            selected_bus = buses[bus - 1]
            print("\nYou selected:", selected_bus)
            print("Now select your seat:")
            bookSeat(selected_bus)   
        else:
            print("Invalid bus option!")

    
    elif route == 2:
        print("\nAvailable buses for your given date and destination are listed below:")

        buses = [
            "VIT TO ASHTA | Bus Number:1211 | Time: 4:15P.M.",
            "VIT TO ASHTA | Bus Number:1213 | Time: 5:15P.M.",
            "VIT TO ASHTA | Bus Number:1220 | Time: 6:15P.M."
        ]

        for i, b in enumerate(buses, start=1):
            print(f"{i}: {b}")

        bus = int(input("Please choose the bus you would like to travel in (1-3) = "))

        if 1 <= bus <= 3:
            selected_bus = buses[bus - 1]
            print("\nYou selected:", selected_bus)
            print("Now select your seat:")
            bookSeat(selected_bus)
        else:
            print("Invalid bus option!")

   
    elif route == 3:
        print("\nAvailable buses for your given date and destination are listed below:")

        buses = [
            "VIT TO SEHORE | Bus Number:1217 | Time: 4:10P.M.",
            "VIT TO SEHORE | Bus Number:1218 | Time: 5:10P.M.",
            "VIT TO SEHORE | Bus Number:1221 | Time: 6:10P.M."
        ]

        for i, b in enumerate(buses, start=1):
            print(f"{i}: {b}")

        bus = int(input("Please choose the bus you would like to travel in (1-3) = "))

        if 1 <= bus <= 3:
            selected_bus = buses[bus - 1]
            print("\nYou selected:", selected_bus)
            print("Now select your seat:")
            bookSeat(selected_bus)
        else:
            print("Invalid bus option!")

    else:
        print("Invalid route selected!")


def Routes():
    print("\nAvailable Routes:")
    print("1: VIT To Bhopal")
    print("2: VIT To Ashta")
    print("3: VIT To Sehore")



def AvlBus():
    print("\nAll Available Buses:")
    print("1: VIT TO BHOPAL | Bus Number:1212 | Time: 4:00P.M.")
    print("2: VIT TO BHOPAL | Bus Number:1214 | Time: 4:30P.M.")
    print("3: VIT TO BHOPAL | Bus Number:1215 | Time: 5:00P.M.")
    print("4: VIT TO BHOPAL | Bus Number:1216 | Time: 5:30P.M.")
    print("5: VIT TO BHOPAL | Bus Number:1219 | Time: 6:30P.M.")
    print("6: VIT TO ASHTA  | Bus Number:1211 | Time: 4:15P.M.")
    print("7: VIT TO ASHTA  | Bus Number:1213 | Time: 5:15P.M.")
    print("8: VIT TO ASHTA  | Bus Number:1220 | Time: 6:15P.M.")
    print("9: VIT TO SEHORE | Bus Number:1217 | Time: 4:10P.M.")
    print("10: VIT TO SEHORE | Bus Number:1218 | Time: 5:10P.M.")
    print("11: VIT TO SEHORE | Bus Number:1221 | Time: 6:10P.M.")


def SeatAvailability():
    print("\nCheck Seat Availability")
    print("First choose route and bus (only viewing, no booking).")

    print("\nRoutes:")
    print("1: VIT To Bhopal")
    print("2: VIT To Ashta")
    print("3: VIT To Sehore")
    route = int(input("Please tell us your destination (1,2,3) = "))

    bus_list = []

    if route == 1:
        bus_list = [
            "VIT TO BHOPAL | Bus Number:1212 | Time: 4:00P.M.",
            "VIT TO BHOPAL | Bus Number:1214 | Time: 4:30P.M.",
            "VIT TO BHOPAL | Bus Number:1215 | Time: 5:00P.M.",
            "VIT TO BHOPAL | Bus Number:1216 | Time: 5:30P.M.",
            "VIT TO BHOPAL | Bus Number:1219 | Time: 6:30P.M."
        ]
    elif route == 2:
        bus_list = [
            "VIT TO ASHTA | Bus Number:1211 | Time: 4:15P.M.",
            "VIT TO ASHTA | Bus Number:1213 | Time: 5:15P.M.",
            "VIT TO ASHTA | Bus Number:1220 | Time: 6:15P.M."
        ]
    elif route == 3:
        bus_list = [
            "VIT TO SEHORE | Bus Number:1217 | Time: 4:10P.M.",
            "VIT TO SEHORE | Bus Number:1218 | Time: 5:10P.M.",
            "VIT TO SEHORE | Bus Number:1221 | Time: 6:10P.M."
        ]
    else:
        print("Invalid route selected!")
        return

    print("\nAvailable Buses:")
    for i, b in enumerate(bus_list, start=1):
        print(f"{i}: {b}")

    try:
        bus = int(input("Please choose the bus (number) = "))
    except ValueError:
        print("Invalid input!")
        return

    if 1 <= bus <= len(bus_list):
        selected_bus = bus_list[bus - 1]
        print("\nShowing seat layout for:", selected_bus)
        showSeats()  
    else:
        print("Invalid bus option!")




while True:

    while True:
        print("\nPlease choose the date you would like to travel")
        try:
            day = int(input("Day = "))
            month = int(input("Month = "))
            year = int(input("Year = "))

            journey_date = datetime.date(year, month, day)
            today = datetime.date.today()

            if journey_date < today:
                print("❌ Invalid Date! Please enter a valid date!!!.\n")
                continue 

            print("\nYour journey date:", journey_date.strftime("%d-%m-%Y"))
            break  
        except ValueError:
            print("❌ Invalid Date! Please enter a valid calendar date.\n")
            continue

    
    while True:
        print("\n=== Main Menu ===")
        print("1: Book Tickets")
        print("2: Check Routes")
        print("3: Check Available Buses")
        print("4: Seat Availability (VIEW ONLY)")
        print("5: Change Date")
        print("0: Exit")

        try:
            menu = int(input("Choose your option (0-5) = "))
        except ValueError:
            print("Invalid option! Please enter a number.")
            continue

        if menu == 1:
            Ticketbooking()      

        elif menu == 2:
            Routes()

        elif menu == 3:
            AvlBus()

        elif menu == 4:
            SeatAvailability()

        elif menu == 5:
            break

        elif menu == 0:
            print("Thank you for using VIT Bus Booking System!")
            exit()

        else:
            print("Invalid option! Try again.")