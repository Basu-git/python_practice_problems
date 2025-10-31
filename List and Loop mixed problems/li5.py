employees = ['Raj', 'Anita', 'Kiran', 'Raj', 'Sunil', 'Kiran']
c=[]
for employee in employees:
    if employees.count(employee)>1 and employee not in c:
        c.append(employee)
print(f"The Names appearing more than once is {c}")
print(f"The unique list of employee {list(set(employees))}")