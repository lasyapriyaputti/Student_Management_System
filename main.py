import pandas as pd
from database import init_files
from operations import New_Student,Lookup_Student,Update_Student_details
def menu():
    print("--- Student Management System ---")
    print("1. Add New Student")
    print("2. Lookup Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5.  Reports for Parent-Teacher Meeting")
    print("6.  Bulk Import")
    print("7. Sort / Filter")
    print("8. Exit")
    return input("Enter your choice: ")

if __name__ == "__main__":
    init_files()
    while True:
        choice = menu()
        if choice == '1':
            New_Student()
        elif choice == '2':
            Lookup_Student()
        elif choice == '3':
            Update_Student_details()
        elif choice == '4':
             print("Still in progress")
        elif choice == '5':
             print("Still in progress")
        elif choice == '6':
             print("Still in progress")
        elif choice == '7':
             print("Still in progress")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")   


