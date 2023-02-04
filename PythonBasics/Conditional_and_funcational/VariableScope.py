# Local Variable

# def func():
#     x = "Local Variable"
#     print(x)

def func():
    global x
    x = x + ", I am local"
    print(x)

x = "global variable"
func()
print(x)