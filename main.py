from os import system as terminal
import mysql.connector as sql
from time import sleep

def connection():
    global cursor
    global connect
    connect = sql.connect(host='127.0.0.1', user='root', password='a3glolop')
    cursor = connect.cursor()
    cursor.execute("create database if not exists Param")
    cursor.execute("use Param")
    cursor.execute("create table if not exists room(number int(2) primary key, type varchar(10), cost int(6), avail int(1) default 1)")
    cursor.execute("create table if not exists customer(number int(2), name varchar(50), total int(2))")
    connect.commit
    if connect.is_connected():
        return True
    else:
        return False

def show(table):
    global cursor
    global connect
    cursor.execute(f"select * from {table}")
    data = cursor.fetchall()
    for x in data:
        print(x)

def add(table):
    global cursor
    global connect
    terminal("cls")
    print(f"{table} Add Menu")
    number = int(input("Number: "))
    if table == "room":
        type = input("Type: ")
        cost = int(input("Cost: "))
        cursor.execute(f"insert into room values({number},'{type}',{cost},1)")
        connect.commit()
    elif table == "customer":
        name = input("Name: ")
        people = int(input("Total People: "))
        cursor.execute(f"insert into customer values({number},'{name}',{people})")
        connect.commit()

def modify(table):
    global cursor
    global connect
    terminal("cls")
    print(f"{table} Modify Menu")
    if table == "room":
        print("1: Update Number: ")
        print("2: Update Type: ")
        print("3: Update Cost: ")
        print("4: Update Availability: ")
        print("5: Return")

        choice = int(input("Choice: "))
        
        if choice == 1: #update number
            old = int(input("Old Number: "))
            new = int(input("New Number: "))
            cursor.execute(f"update room set number={new} where number={old}")
            connect.commit()

        elif choice == 2: #update type
            number = int(input("Room Number: "))
            new = input("New Type: ")
            cursor.execute(f"update room set type='{new}' where number={number}")
            connect.commit()

        elif choice == 3: #update cost
            number = int(input("Room Number: "))
            new = int(input("New Cost: "))
            cursor.execute(f"update room set cost={new} where number={number}")
            connect.commit()
        
        elif choice == 4:
            number = int(input("Room Number: "))
            new = int(input("Availability: "))
            cursor.execute(f"update room set avail={new} where number={number}")
            connect.commit()
        
        elif choice == 5:
            return
    
    elif table == "customer":
        print("1: Update Number")
        print("2: Update Name")
        print("3: Update Total")
        print("4: Return")

        choice = int(input("Choice: "))

        if choice == 1:
            old = int(input("Old Number: "))
            new = int(input("New Number: "))
            cursor.execute(f"update customer set number={new} where number={old}")
            connect.commit()
        
        elif choice == 2:
            old = input("Old Name: ")
            new = input("New Name: ")
            cursor.execute(f"update customer set name='{new}' where name='{old}'")
            connect.commit()
        
        elif choice == 3:
            old = int(input("Old: "))
            new = int(input("New: "))
            cursor.execute(f"update customer set total={new} where total={old}")
            connect.commit()
        
        elif choice == 4:
            return

def delete(table):
    global cursor
    global connect
    number = int(input("Room Number: "))
    cursor.execute(f"delete from {table} where number = {number}")
    connect.commit()

def table(table):
    while True:
        terminal("cls")
        print(f"{table} Menu")
        print("1: Add")
        print("2: Modify")
        print("3: Delete")
        print("4: Show")
        print("5: Return")

        choice = int(input("Choice: "))
        if choice == 1:
            add(table)
        elif choice == 2:
            modify(table)
        elif choice == 3:
            delete(table)
        elif choice == 4:
            show(table)
        elif choice == 5:
            return

def main():
    while True:
        terminal("cls")
        print("Main Menu")
        print("1: Room")
        print("2: Customer")
        print("3: Exit")

        choice = int(input("Choice: "))
        if choice == 1:
            table("room")
        elif choice == 2:
            table("customer")
        else:
            break

if connection():
    main()
