username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()

x = 99
# def func2(y):
#     z = x + y
#     return z
# print(func2(1))

# def func3():
#     global x    #it works, but it should be avoided
#     x = 12

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()    #the variable name works hierarchly, it first looks in itself and then looks outside it, and then globally 

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1() #this prints 88, when f2 is returned, it packs all the memory references with itself. This is called closure

