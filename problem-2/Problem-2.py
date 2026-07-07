employees = [
    {"name":"Ali","salary":900},
    {"name":"Sara","salary":1400},
    {"name":"Ahmad","salary":2100},
    {"name":"Lina","salary":1500}
]
def find_max_salary (employees:list):
    max=-999
    for employee in range(len(employees)):
        if employees[employee]["salary"]>max:
         max=employees[employee]["salary"]
    print(max)
##to find the max salary
find_max_salary(employees)

def find_avg_salary (employees:list):
    sum=0
    for employee in range(len(employees)):
        sum+=employees[employee]["salary"]
    print(sum/len(employees))


##to find the avg salary
find_avg_salary(employees)
