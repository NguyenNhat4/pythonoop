# Xây dựng hệ thống quản lý nhân viên công ty:

# 1. Tạo class Employee với:
#    - Attributes: name, employee_id, base_salary
#    - Method calculate_salary() (return base_salary)
#    - Method work() (in "Working...")

# 2. Tạo 2 class con:
   
#    a) Manager(Employee):
#       - Thêm attribute: team_size
#       - Override calculate_salary(): 
#         base_salary + (team_size * 500000) [bonus theo số người quản lý]
#       - Override work(): "Managing team of {team_size}"
   
#    b) Developer(Employee):
#       - Thêm attribute: programming_language
#       - Override calculate_salary(): 
#         base_salary + 2000000 [tech bonus]
#       - Override work(): "Coding in {programming_language}"

# 3. Tạo ít nhất:
#    - 2 developers
#    - 1 manager
#    - In ra thông tin và lương của từng ngườia

class Employee:
    def __init__(self,name,employee_id,base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def caculate_salary(self):
        return self.base_salary
    
    def work(self):
        print(f"{self.name} in working")


class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, team_size):
        self.team_size = team_size
        super().__init__(name, employee_id, base_salary)

    def caculate_salary(self):
        return self.base_salary + self.team_size * 500000
    
    def work(self):
        print(f"Managing team of {self.team_size} people.")

# a = Manager("Huy", "A", 100000, 200000)
# b = Manager("Linh","B", 80000, 150000)

# a.work()
# b.work()
# a.caculate_salary()
# b.caculate_salary()

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language):
        super().__init__(name, employee_id, base_salary)
        self.programming_language = programming_language
    
    def calculate_salary(self):
        return self.base_salary + 2000000
    
    def work(self):
        print(f"Coding in {self.programming_language}")

# dev1 = Developer("Alex","A",100000, "Python")
# dev2 = Developer("Alice", "B", 80000, "C++")
# manager = Manager("Bob", "C", 120000, team_size = 5)

list_people = [Developer("Alex","A",100000, "Python"),Developer("Alice", "B", 80000, "C++"),Manager("Bob", "C", 120000, team_size = 5)]
for people in list_people:
    print(f"{people.name} has salary of {people.caculate_salary()}")

