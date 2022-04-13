#Exercise #4
#Write a recursive function to perform the fibonacci sequence up to the number passed in.
class Fibo (object):
    def __init__(self):
        self.fibonacciList = [1, 1]
        self.counter = 0

    def fibonacci (self, fib):
        recursion = fib
        newFib = self.fibonacciList[-1] + self.fibonacciList[-2]
        self.fibonacciList.append(newFib)
        self.counter = self.counter + 1
        if self.counter < recursion:
            return self.fibonacci(fib)
            
            
        else: 
            return self.fibonacciList


fibo = Fibo()
fib = int(input("How many recursions would you like? "))
print (fibo.fibonacci(fib))