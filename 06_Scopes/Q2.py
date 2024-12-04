#another example of closure

#known as factory functions in Python, used a lot in Django
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)    #now f has the function definition of 'actual' as chaicoder returns the function 'actual'. 'actual' has not been called
g = chaicoder(3)
print(f(3))     #the value 3 is passed into actual and this gives 9
print(g(3))     #similarly this gives 27