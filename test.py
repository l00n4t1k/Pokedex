import test2

print("hi!"*3)

# what is the result of this statement?
theBeaver = "furry"

if theBeaver is not "shaved":
    print("walk away")
else:
    print("helloWorld!")

# how do you print a string of the type of a variable?
a = [2, 4, "t", 3.9]
print(type(str(a)))

var = [1, 2, 3, 4, 5, 6, 7, 9, 10, 24, 25]
print([v for v in var[3:10]])

print(test2.testvar1)
testvar1 = "hello"
print(testvar1)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for index, fibonacci_number in enumerate(fib()):
    print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
