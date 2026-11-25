import mysql.connector
mydbint=mysql.connector.connect(host='localhost',user='root',password='12345678')
mycursor=mydbint.cursor()

try: #check if database exists or not, if not create a new database
    mycursor.execute("CREATE DATABASE car_rental")
    print("Database created successfully")
except:
    print("Database already exists")
    mycursor.execute("USE car_rental")

try: #check if table exists or not, if not create a new table
    mycursor.execute("CREATE TABLE car (eno INT primary key, make VARCHAR(255), year INT, brand VARCHAR(255), price INT, qnty INT)") 
    mycursor.execute("CREATE TABLE member (Mno int primary key,Mname varchar(255),Tel int ,Age int ,Car_no int)")
    print("Table created successfully")
except:
    print("Table already exists")



def main_menu(): # main menu function
    print("welcome to car rental Mangement system")
    print("choose your option")
    print("--------------------------------")
    print("0. Show cars available")
    print("1. Add a new Data")
    print("2. Search")
    print("3. Rent a car") # with bill 
    print("4. Return a car")
    print("5. update member details")
    print("6. delete a member")
    print("7. view report's") # not sure
    print("8. Exit")
    print("--------------------------------")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Please enter a number.")
        main_menu()

    print("You selected option: ", choice)
    print("--------------------------------")


    # choice condition below 
    if choice == 0:
        show_cars_available()
    elif choice == 1: 
        add_data()
    elif choice == 2:
        search()
    elif choice == 3:
        rent_car()
    elif choice == 4:
        return_car()
    elif choice == 5:
        update_member()
    elif choice == 6:
        delete_member()
    elif choice == 7:
        view_reports()
    elif choice == 8:
        exit()
    else:
        print("Invalid choice")
        main_menu()



# option 0 (show cars available) function to be added later
def show_cars_available():
    print("Show cars available")
    mycursor.execute("SELECT * FROM car_rental.car")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    main_menu() 



#option 1 (add a new data) function to add a new member or car
def add_data():
    print("Add a new Data")
    print("1. Add a new member")
    print("2. Add a new car")
    print("3. Back to main menu")
    choice = input("Enter your choice: ")

    if choice == 1:
        add_member()
    elif choice == 2:
        add_car()
    elif choice == 3:
        main_menu()
    else:
        print("Invalid choice")
        main_menu()

def add_member():#function to add a new member
    print("Add a new member")
    member_no = input("Enter member number: ")
    name = input("Enter member name: ")
    phone = input("Enter member phone number: ")
    age = input("Enter member Age: ")
    car_no = input("Enter member car number: ")

    try:
        query= "INSERT INTO car_rental.member (member_no, name, phone, age , car_no)"
        val = (member_no, name, phone, age, car_no)
        mycursor.execute(query, val)
        mydbint.commit()
        main_menu()
    except:
        print("Error occurred while adding member")
        main_menu()

def add_car(): #function to add a new car
    print("Add a new car")
    car_no = input("Enter car number: ")
    make = input("Enter car make: ")
    year = input("Enter car year: ")
    brand = input("Enter car brand: ")
    price = input("Enter Price: ")
    qnty = input("Enter number of cars: ")

    try:
        query= "INSERT INTO car_rental.car (car_no, make, year, brand, price, qnty)"
        val = (car_no, make, year, brand, price, qnty)
        mycursor.execute(query, val)
        mydbint.commit()
        main_menu()
    except:
        print("Error occurred while adding car")
        main_menu()



#option 2 (search) function to search for a member or car
def search(): #function to search for a member or car
    print("Search")
    print("1. Search for a member")
    print("2. Search for a car")
    print("3. Back to main menu")
    choice = input("Enter your choice: ")

    if choice == 1:
        search_member()
    elif choice == 2:
        search_car()
    elif choice == 3:
        main_menu()
    else:
        print("Invalid choice")
        main_menu()

def search_member(): #function to search for a member
    print("Search for a member")
    member_no = input("Enter member number: ")
    query = "SELECT * FROM car_rental.member WHERE member_no = %s"
    val = (member_no,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print("Member found: ", result)
    else:
        print("Member not found")
    main_menu()

def search_car(): #function to search for a car
    print("Search for a car")
    car_no = input("Enter car number: ")
    query = "SELECT * FROM car_rental.car WHERE car_no = %s"
    val = (car_no,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print("Car found: ", result)
    else:
        print("Car not found")
    main_menu()



#option 3 (rent a car) function to rent a car
def rent_car(): #function to rent a car
    print("Rent a car")
    member_no = input("Enter member number: ")
    car_no = input("Enter car number: ")
    query = "SELECT * FROM car_rental.car WHERE car_no = %s"
    val = (car_no,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print("Car found: ", result)
        qnty = result[5]
        if qnty > 0:
            qnty -= 1
            query = "UPDATE car_rental.car SET qnty = %s WHERE car_no = %s"
            val = (qnty, car_no)
            mycursor.execute(query, val)
            mydbint.commit()
            print("Car rented successfully")
        else:
            print("Car not available")
    else:
        print("Car not found")
    main_menu()



#option 4 (return a car) function to return a car with bill
def return_car(): #function to return a car
    print("Return a car")
    member_no = input("Enter member number: ")
    car_no = input("Enter car number: ")
    query = "SELECT * FROM car_rental.car WHERE car_no = %s"
    val = (car_no,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print("Car found: ", result)
        qnty = result[5]
        qnty += 1
        query = "UPDATE car_rental.car SET qnty = %s WHERE car_no = %s"
        val = (qnty, car_no)
        mycursor.execute(query, val)
        mydbint.commit()
        print("Car returned successfully")
        # bill fuction will add later
    else:
        print("Car not found")
    main_menu()



#option 5 (update member details) function to update member details
def update_member(): #function to update member details
    print("Update member details")
    member_no = input("Enter member number: ")
    query = "SELECT * FROM car_rental.member WHERE member_no = %s"
    val = (member_no,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print("Member found: ", result)
        name = input("Enter new member name: ")
        phone = input("Enter new member phone number: ")
        age = input("Enter new member Age: ")
        car_no = input("Enter new member car number: ")
        query = "UPDATE car_rental.member SET name = %s, phone = %s, age = %s, car_no = %s WHERE member_no = %s"
        val = (name, phone, age, car_no, member_no)
        mycursor.execute(query, val)
        mydbint.commit()
        print("Member details updated successfully")
    else:
        print("Member not found")
    main_menu()



#option 6 (delete a member) function to delete a member
def delete_member(): #function to delete a member
    print("Delete a member")
    member_no = input("Enter member number: ")
    query = "SELECT * FROM car_rental.member WHERE member_no = %s"
    val = (member_no,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print("Member found: ", result)
        query = "DELETE FROM car_rental.member WHERE member_no = %s"
        val = (member_no,)
        mycursor.execute(query, val)
        mydbint.commit()
        print("Member deleted successfully")
    else:
        print("Member not found")
    main_menu()



#option 7 (view reports) function to view reports
def view_reports(): #function to view reports
    print("View reports")
    print("1. View all members")
    print("2. View all cars")
    print("3. Back to main menu")
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Please enter a number.")
        view_reports()

    if choice == 1:
        view_all_members()
    elif choice == 2:
        view_all_cars()
    elif choice == 3:
        main_menu()
    else:
        print("Invalid choice")
        main_menu()

def view_all_members(): #function to view all members
    mycursor.execute("SELECT * FROM car_rental.member")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    main_menu()

def view_all_cars(): #function to view all cars
    mycursor.execute("SELECT * FROM car_rental.car")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    main_menu()



#option 8 (exit) function to exit the program
def exit(): # option 8 function to exit the program
    print("Exiting the program")
    mydbint.close() # close the database connection
    quit()


main_menu() # call main menu function to start the program
# Car rental managment software group project 10 