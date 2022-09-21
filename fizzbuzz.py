# function that can only take one number as an argument
def fizz_buzz_fizzbuzz(num):
#   having 3/5 fizzbuzz first ensures the top down code will catch if both instead of stopping at just one or the other
        if (num % 3 == 0 and num % 5 == 0):
            print('fizzbuzz', num)
        elif (num % 5 == 0):
            print('buzz', num)
        elif (num % 3 == 0):
            print('fizz', num)
  
    
      
        

# the list of numbers needs to be looped through so function can take one at a time
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in list:
    # call the function using the number in the looped list
    fizz_buzz_fizzbuzz(num)




