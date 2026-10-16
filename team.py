employees=[
    {"name":"Anu","salary":30000},
    {"name":"Ravi","salary":42000},
    {"name":"Meena","salary":35000}
]


def high_earners(people,limit):
    for employee in people:
        if employee["salary"]>limit:
            print(employee["name"],employee["salary"])
high_earners(employees,40000)
