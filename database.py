import pandas as pd
import os
CSV_FILE="data/students.csv"
EXCEL_FILE = "data/students.xlsx"
if not os.path.exists("data"):
    os.makedirs("data")
    
def init_files():
    if not os.path.exists(CSV_FILE):
        columns = ["Roll_No", "Name", "Branch", "Year", "Gender", "Age",
                   "Attendance_%", "Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]
        df = pd.DataFrame(columns=columns)  
        df.to_csv(CSV_FILE, index=False)
        df.to_excel(EXCEL_FILE, index=False)  
    else:
        df = pd.read_csv(CSV_FILE)          
        df.to_excel(EXCEL_FILE, index=False)

def save(df):
    df.to_csv(CSV_FILE,index=False)
    df.to_excel(EXCEL_FILE,index=False)
