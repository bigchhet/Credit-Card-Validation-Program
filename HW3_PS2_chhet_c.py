#Chhai Chhet
#1239352
#Homework 3 Program Set 2
#This program is a Credit card number validation Program using functions


#define the main function
def main():

    #user will input the credit card number as a string
    checkAmount = int(input("How many credit card numbers do you want to check? "))

    #put user in for loop and prompt them to enter a credit card number
    for x in range(checkAmount):

        #call the function isValid() and print whether the credit card number is valid or not valid
        number = input("Enter a credit card number: ")

        #declare variables for upper and lower parameters
        size = len(number)
        lower = 13
        upper = 16
        
        #ensure that the credit card number entered is within 13-16 digits
        if((size >= lower) and (size <= upper)):

            #call isValid function to further investiage validity of credit card
            if(isValid(number) == True):
                print(number + " is valid")

            #this code will execute if the credit card number is within 13-16 digits but does not meet the other requirements for being valid
            else:
                print(number + " is invalid")
            
        #if not within the specified range, automatically not valid.
        else:
            print(number + " is invalid")
        
        #adding space for better readibility after each iteration of for loop
        print()

#define isValid function to be in charge of investigating the validity of user input credit card
def isValid(number):

    #set the value of check variable to False, which will only become true if determined valid
    check = False

    #logic for checking if the credit starts with 4, 5, 37, 6
    if( (number.startswith("4")) or (number.startswith("5")) or (number.startswith("37")) or (number.startswith("6"))):
        
        #call necessary functions and save values
        totalEven = sumOfDoubleEvenPlace(number)
        totalOdd = sumOfOddPlace(number)

        #simple arithmetic using the returned values from calling functions and storing it into a new final variable
        final = (totalEven + totalOdd)
        
        #if the remainder of dividing final by 10 is 0, then set the check variable to true
        if(final % 10 == 0):
            check = True

    #this code will run if the credit card number the user enters does not begin with the specified numbers        
    else:
        #keeps check remaining false
        check = False
        
    #at the end of running the function, return check boolean back to caller
    return check


#define the sumOfDouble function tobe in charge of calculating the sum of each digit of credit card number 
def sumOfDoubleEvenPlace(cardNumber):

    #declare the local variables necessary to run function
    total = 0
    end = (len(cardNumber))

    #logic for calculating total sum of evenplace digits
    for i in range(end - 1, 0, -2):

        #this log is used to accurate position of targeted cardNumber position
        current = cardNumber[i - 1]

        #getDigit is used to determine if splitting is needed, and aids in finding total sum of credit card in even position
        total = total + getDigit(current)

    #after the function has gone through its iteration, return the variable total to its inital caller    
    return total


#define sumOfOddPlace function to determine the sum of call the odd digits in the credit card        
def sumOfOddPlace(cardNumber):

    #declare necessary variables to run function
    total = 0
    end = (len(cardNumber)-1)
    
    #logic for calculating total sum of oddplace digits
    for i in range(end, -1, -2):

        #set the current variable equal to the string index of current credit card position
        current = cardNumber[i]

        #convert that current position from string into integer and add it to the running total value
        total = total + int(current)
    
    #at the end of the function return the total variable back to the caller
    return total


#getDigit function is used to determine whether or not a digit needs to be split and added or continue normal arithmetic
def getDigit(number):

    #double the value of the inputted number and save into a local variable while also converting its data type
    value = int(number) * 2

    #if the length of the converted value is greater than 1, split the digits and add them
    if (len(str(value)) == 2):

        #revert value variable back into a string to get their indexes
        value = str(value)

        #get value for the first digit and save into local variable
        digit1 = (value[0])
        #get value for the second digit and save into local variable
        digit2 = value[1]
        #convert the local variables into integers and perform simple addittiton to save into value 
        value = int(digit1) + int(digit2)

    #return the value variable to its inital caller
    return value


#tells program what to call first
if __name__ == "__main__":
    main()








#----------------------------OUTPUT-----------------------------------

#TEST 1
#How many credit card numbers do you want to check? 2
#Enter a credit card number: 4388576018402626
#4388576018402626 is invalid
#
#Enter a credit card number: 4388576018410707
#4388576018410707 is valid



#TEST 2
#How many credit card numbers do you want to check? 0



#TEST 3
#How many credit card numbers do you want to check? 3
#Enter a credit card number: 12345678
#12345678 is invalid
#
#Enter a credit card number: 5169769005222217
#5169769005222217 is valid
#
#Enter a credit card number: 6011655276746808
#6011655276746808 is invalid



#TEST 4
#How many credit card numbers do you want to check? 4
#Enter a credit card number: 5215401083674317
#5215401083674317 is valid
#
#Enter a credit card number: 55555555555555
#55555555555555 is invalid
#
#Enter a credit card number: 6011668425281035
#6011668425281035 is valid
#
#Enter a credit card number: 6011668425111
#601166842528103 is invalid



#TEST 5
#How many credit card numbers do you want to check? 3
#Enter a credit card number: 373075504003782
#373075504003782 is valid
#
#Enter a credit card number: 373075504003754
#373075504003754 is invalid
#
#Enter a credit card number: 373075504003728
#373075504003728 is invalid
