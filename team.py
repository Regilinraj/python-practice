employees=[
    {"name":"Anu","salary":30000},
    {"name":"Ravi","salary":42000},
    {"name":"Meena","salary":35000}
]
for employee in employees:
    if employee["salary"]>30000:
        print(employee["name"],employee["salary"])
