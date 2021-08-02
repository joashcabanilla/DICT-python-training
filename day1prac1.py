employeeName = str(input("Enter Employee Name:"))
hoursNumber = float(input("Enter number of hours rendered: "))
hoursRate = float(input("Enter rate per hour: "))
GSIS = float(input("GSIS Premium: "))
philHealth = float(input("PhilHealth: "))
housingLoan = float(input("Housing Loan: "))
taxRate = float(input("Tax rate: "))

grossSalary = hoursNumber * hoursRate
taxRate = taxRate / 100
taxGrossSalary = grossSalary * taxRate
totalDeduct = GSIS + philHealth + housingLoan + taxGrossSalary
netSalary = grossSalary - totalDeduct

print(f"\n\nGross Salary: {grossSalary}")
print(f"Total deductions: {totalDeduct}")
print(f"Net Salary: {netSalary}")




