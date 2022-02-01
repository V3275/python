print("Please give me a range to work with.")

#catches unexpected errors 
try :
    i = int(input("Please enter the initial number : "))
    n = int(input("Please enter the final number : "))
except :
    print("Please enter a number.")
    
#creates a list with given input as range() arguments.    
range_list = list(range(i, n+1))

#a function to call upon the created list.
def fizzbuzz(range_list) :
    for num in range_list :
        if (num % 3 == 0) &(num % 5 == 0) :
            print("FizzBuzz")
        elif (num % 3 == 0) :
            print("Fizz")
        elif (num % 5 == 0) :
            print("Buzz")
        else :
            print(num)

fizzbuzz(range_list)
