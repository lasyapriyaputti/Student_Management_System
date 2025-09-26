import pandas as pd
from database import CSV_FILE,save

def New_Student():
    try:
         Roll_No=int(input("Enter Roll_No: "))
    except ValueError:
        print("Enter valid value")     
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = int(input("Enter Year: "))
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    attendance = int(input("Enter Attendance (0-100): "))
    if attendance<0 or  attendance>100:
        print("Enter valid value")
        return
    mid1 = int(input("Enter Mid1 Marks (0-100): "))
    if mid1<0 or  mid1>100:
        print("Enter valid value")
        return
    mid2 = int(input("Enter Mid2 Marks (0-100): "))
    if mid2<0 or  mid2>100:
        print("Enter valid value")
        return
    quiz = int(input("Enter Quiz Marks (0-20): "))
    if quiz<0 or  quiz>20:
        print("Enter valid value")
        return
    final = int(input("Enter Final Marks (0-100): "))
    if final<0 or  final>100:
        print("Enter valid value")
        return

    student = {
    "Roll_No": Roll_No,
    "Name": name,
    "Branch": branch,
    "Year": year,
    "Gender": gender,
    "Age": age,
    "Attendance_%": attendance,
    "Mid1_Marks": mid1,
    "Mid2_Marks": mid2,
    "Quiz_Marks": quiz,
    "Final_Marks": final
    }
    df = pd.read_csv(CSV_FILE) 
    df = pd.concat([df, pd.DataFrame([student])], ignore_index=True)
    save(df)
    print("Record updated successfully!")

def Lookup_Student():
    df=pd.read_csv(CSV_FILE)
    choice=input("Lookup_Student using Name(1) or Lookup_Student using Roll_No(2) Enter Your Choice:")
    if choice=="1":
        Name=input("Enter Name:")
        result=df[df["Name"].str.contains(Name,case=False)]
    elif choice=="2":
        Roll_No=int(input("Enter Roll_No:"))
        result=df[df["Roll_No"]==Roll_No] 
    else:
        print("Invalid Choice:")     

    if not result.empty:
        print(result)
    else :
        print("Student not found")    
       







