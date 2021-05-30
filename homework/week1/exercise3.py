float_var = 8.98
int_var = 4
str_var = "Jam"
print(f"{str_var.upper()}")
print(f"{round(float_var,1)}")

#print(dir(int_var))
#dir(int_val) prints out directory of int methods
print(f"Negative int_var is:{int_var.__neg__()}")
#__neg__() returns negative value of variable
#print(dir(float_var))
print(f"float_var rounded to nearest whole number is:{float_var.__round__(1)}")