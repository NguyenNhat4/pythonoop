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
#    - In ra thông tin và lương của từng người