
name="Senanur"
surname="Yurtseven"
age=23

print("My name is {}".format(name))

print("My name is {}{}".format(name, surname))  

print("My name is {1}{0}".format(name,surname)) #Here , whichever one we want to write first,instead of swapping their positions,,we can specify it as the zero index.

print("My name is {n}{s}".format(n=name, s=surname))

print("My name is {s}{n}".format(n=name, s=surname)) #Here use can assign nicknames using name and surnmae. For example, ıf we represent name with n and surname s.

print("My name is {s}{n}".format(n=name, s=surname)) #we cab also display them in any order we want.

print("My name is {}{} I'm {}years old".format(name, surname,age))  
print("My name is {0}{1} I'm {2}years old".format(name, surname,age))  
print("My name is {1}{0} I'm {2}years old".format(name, surname,age))  

number=12/3

print("the result is {n:1.4}".format(n=number))

print(f"My name is {name} {surname}")