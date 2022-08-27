# David Prato CIS 261 Iteration And Recursion Lab

def fac_rec(num):
    if num == 0 or num == 1: #Setting up our exit mode
        return 1
    else: 
        return num * fac_rec(num -1) # recalling our function with our input minus 1
        # ex (5) lists 1 * 2 * 3 * 4 * 5 (before returning 1) = 120

def fac_iter(num):
    fact = 1 #we start with 1
    for number in range(2, num + 1):# remember the range function is range (start, stop) so we start at 2, and go to num +1 so in the case of 5,the range runs from 2 to 5
        fact = number * fact # ex (5): 2 * 1 = 2, 3 * 2 = 6, 4 * 6 = 24, 5 * 24 = 120
    return fact

def main():
    numList = [0, 5, 10, 25, 50, 100] # this gives our num from this list
    print("Factorial results using an iterative function")
    for num in numList:
        print(f'{num}! =  {fac_iter(num)}') # calls iteration function
    print()
    print ("Factorial reults using a recursive function") 
    for num in numList:
        print(num, '! = ', fac_rec(num))# calls recursive functions

if __name__ == "__main__":
    main()
