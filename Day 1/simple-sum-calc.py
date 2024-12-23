#Total students Calculator:

std1 = int(input('Enter number of Male Students: '))
std2 = int(input('Enter number of Female Students: '))
std3 = int(input('Enter number of Trans Students: '))
std4 = int(input('Enter number of Absent Students: ')) 
total_std = std1 + std2 + std3 - std4
print(f'Total number of students: {total_std}')