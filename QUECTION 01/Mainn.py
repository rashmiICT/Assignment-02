from Array import stack

mystack = stack()

print("===================================================")
mystack.isEmpty()
print("===================================================\n")



print("~~~~~~~~~~~~~~~~~~PUSH ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
print("===================================================\n")




print("~~~~~~~~~~~~~~~~~~TOP ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.top()
print("==================================================\n")




print("~~~~~~~~~~~~~~~~~~STACK LENGTH~~~~~~~~~~~~~~~~~~~~~~~\n")
x = mystack.size()
print("STACK LENGTH IS ", x)
print("===================================================\n")




print("~~~~~~~~~~~~~~~~~~POP ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.pop()
print("===================================================\n")




print("~~~~~~~~~~~~~~~~~~STACK LENGTH~~~~~~~~~~~~~~~~~~~~~~~\n")
x = mystack.size()
print("STACK LENGTH IS ", x)
print("===================================================\n")





print("~~~~~~~~~~~~~~~~~~ STACK FULL OR NOT~~~~~~~~~~~~~~~~~\n")
mystack.isFull()
print("===================================================\n")





print("~~~~~~~~~~~~~~~~~~POP ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.pop()
mystack.pop()
mystack.pop()
print("===================================================\n")




print("~~~~~~~~~~~~~~~~~~TOP ELEMENT~~~~~~~~~~~~~~~~~~~~~~~\n")
mystack.top()
print("==================================================\n")




print("~~~~~~~~~~~~~~~~~~STACK LENGTH~~~~~~~~~~~~~~~~~~~~~~~\n")
x = mystack.size()
print("STACK LENGTH IS ", x)
print("===================================================\n")




mystack.push(50)
mystack.push(60)
