import pandas as pd

data = {
    "RollNo": range(1, 21),
    "Name": ["A"+str(i) for i in range(1,21)],
    "Gender": ["Male","Female"]*10,
    "E-Mail": ["a"+str(i)+"@gmail.com" for i in range(1,21)],
    "Mobile": ["98765432"+str(i).zfill(2) for i in range(10,30)],
    "Age": [20+i%5 for i in range(20)],
    "City": ["Rajkot","Ahmedabad"]*10
}

df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)


df = pd.read_excel("students.xlsx")

print(df.columns)   # Column names
print(df.dtypes)    # Data types
