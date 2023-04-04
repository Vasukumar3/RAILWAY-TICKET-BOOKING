# This program simulates booking train tickets. It has four classes: Train, Passenger, Ticket and Account.

# The Train class represents a train with its train number, source, destination, and the number of seats available. It has methods to display the train information and book tickets.

# The Passenger class represents a passenger with their name, age, gender, and phone number. It has a method to display passenger information.

# The Ticket class represents a ticket with the train, source, destination, passengers, and PNR (Passenger Name Record) number. It has a method to display ticket information.

# Class called Account is defined with a constructor that takes two arguments: username and password. The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password.

# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------

import random
# We start by importing the random module, which we'll use to generate random PNRs for the tickets later on.


class Train():
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats

#     We define the Train class, which takes in four parameter a train number, source, destination, and number of available seats. The __init__() method is called when a new Train object is created and initializes these attributes.

    def display_info(self):
        print(f"Train number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available seats: {self.seats}")
        print()  # line break for each train information is displayed

#     We define a display_info() method for the Train class, which displays the train number, source, destination, and number of available seats for a given train object.

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.seats -= num_tickets
            return pnr_list

#     We define a book_tickets() method for the Train class, which takes a number of tickets as input and attempts to book that many tickets on the train. If there are enough available seats, the method generates a list of random PNRs equal to the number of tickets being booked, updates the number of available seats, and returns the list of PNRs. Otherwise, the method returns None to indicate that the booking failed.
# The book_tickets method takes in the number of tickets to be booked and returns a list of PNR numbers for the tickets if they are available, or None if there are not enough seats.


class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
# The Passenger class is defined, which takes in four parameters - name, age, gender, and phone. These parameters are used to initialize the attributes of the Passenger object.

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")
# The Passenger class has a method called display_info, which prints out the name, age, gender, and phone number of the passenger.


class Ticket:
    def __init__(self, train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
# The Ticket class is defined, which takes in five parameters - train, source, destination, passengers, and pnr. These parameters are used to initialize the attributes of the Ticket object.

    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR: {self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()
# The Ticket class has a method called display_info, which prints out the train number, source, destination, PNR number, and the information of each passenger.


class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


# Class called Account is defined with a constructor that takes two arguments: username and password. These arguments are used to initialize instance variables with the same names. The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password.

accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

# A list called accounts is initialized with two Account objects already in it, with the usernames "user1" and "user2" and passwords "password1" and "password2" respectively.

logged_in_account = None
# A variable called logged_in_account is initialized to None. This variable will be used later to keep track of the currently logged-in account.

while True:  # A while loop is started that will run indefinitely until the user logs in successfully and is presented with the available train details.
    print("\n1. Create an account\n2. Login\n")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        accounts.append(Account(username, password))
# If the user chooses to create an account (choice == "1"), they are prompted to enter a username and password. The inputted username and password are then used to create a new Account object, which is appended to the accounts list.
        print("Account created successfully!")
# Inside the loop, the user is presented with two options: either to create an account or to login. The user's choice is stored in a variable called choice.
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid username or password.")
# If the user chooses to login (choice == "2"), they are prompted to enter a username and password. The program then iterates through the accounts list and checks if any of the stored accounts match the inputted username and password. If a match is found, the corresponding Account object is assigned to the logged_in_account variable and the loop is broken. Otherwise, an error message is printed.
        else:
            print(
                f"\nLogged in as {logged_in_account.username}\n\n-----Availabe Train details-----\n")

            break
    else:
        print("Invalid choice.")

if logged_in_account is not None:
    trains = [
        Train("12737", "Tadepalligudem", "Secunderabad", 40),
        Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
        Train("22863", "Vijayawada", "Bangalore", 1)
    ]
# The program creates a list of Train objects, with each train having a unique train number, source, destination, and the number of seats available.

# Display available trains
for train in trains:
    train.display_info()
# If the logged_in_account variable is not None, it means that the user has successfully logged in. A message is printed confirming the login, and then a list of available train details is printed.


# Get user input for booking
while True:
    try:
        train_num = input("Enter Train Number: ")
        num_tickets = int(input("Enter Number of Tickets: "))
        if num_tickets <= 0:
            raise ValueError("Number of tickets should be greater than 0")
        for train in trains:
            if train.train_num == train_num:
                if num_tickets > train.seats:
                    raise ValueError(
                        "Selected more tickets than available seats")  # If the number of tickets entered is more than the available seats, it will raise a ValueError with the message "Selected more tickets than available seats".
                break
        else:
            raise ValueError("Invalid Train Number.")
        break
    except ValueError as e:
        print(f"Invalid Input: {e}")
# The program asks the user to enter the train number and the number of tickets they want to book.

train = None
for t in trains:
    if t.train_num == train_num:
        train = t
        break
# The program then searches for the Train object with the corresponding train number entered by the user.

if train is None:
    print("Invalid Train Number.")
# If the train number is invalid, the program prints "Invalid Train Number." and exits.

else:
    passengers = []
    for i in range(num_tickets):
        print(f"\nEnter details for Passenger {i + 1}:")
        while True:
            try:
                name = input("Name: ")
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age: "))
                if age <= 0 or age > 120:
                    raise ValueError("Invalid Age")
                gender = input("Gender: ")
                phone = input("Phone Number: ")
                if not phone or len(phone) != 10 or not phone.isdigit():
                    raise ValueError("Invalid Phone Number")
                passenger = Passenger(name, age, gender, phone)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")
# If the train number is valid, the program prompts the user to enter the details of each passenger.
# For each passenger, the program creates a Passenger object with the name, age, gender, and phone number entered by the user and appends it to a list of passengers.

    pnr_list = train.book_tickets(num_tickets)
    if pnr_list is None:
        print("Tickets not available.")
# The program then calls the book_tickets method of the Train object to book the tickets. If there are enough seats available, the book_tickets method returns a list of PNR numbers for the tickets, which the program saves in a list called pnr_list.
# If there are not enough seats available, the book_tickets method returns None, and the program prints "Tickets not available." and exits.
    else:
        print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

        for i in range(num_tickets):
            ticket = Ticket(train, train.source, train.destination, [
                            passengers[i]], pnr_list[i])
            ticket.display_info()
            print("\n--------Thank You------- \n-------Safe Journey------")


# If the tickets are successfully booked, the program prints "Booking Successful!" and creates a Ticket object for each passenger with the train, source, destination, passenger information, and PNR number. The program then calls the display_info method of each Ticket object to display the information to the user.


# -------- FINISHED--------
