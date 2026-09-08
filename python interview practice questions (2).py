

#qus 1:

def reverse_string (string:str)->str:
    """this function reverses a given string.
        args:
            Takes only a string as an argument
        returns:
            Returns the given string in reverse order."""

    if not isinstance(string,str):
        raise TypeError ("The input should only be a string.")

    reverse = ""

    for char in string:
        reverse = char + reverse
    return reverse

if __name__ == "__main__" :

    try:
        user_input = input("enter the string:")
        result = reverse_string(user_input)
        print(result)

    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)





#qus 2:

def largest_value (large:list[float])->float:
    """this function gives the largest value from the given list.
        args:
            Takes a integer as list input.
        returns:
            Returns the largest value given in the list."""

    if not isinstance(large,list):
        raise TypeError ("The input should only be an integer.")


    largest = list1[0]

    for num in list1:
        if num > largest:
            largest = num
    return (largest)

if __name__ == "__main__":

    try:
        list1 = [7,5,8,2,10,9]
        result = largest_value(list1)
        print(result)

    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)




#qus 3:

def prime_number_finder (num:int)->int:
    """this function gives tells about if the given number is prime number or not.
        It takes input from user and checks whether the number is prime number or not.

        returns:
            Returns whether number is prime or not prime."""

    if not isinstance(num,int):
        raise TypeError ("The input should only be an integer.")

    for i in range (2,num):
        if num % i == 0:
            return("The given number is not a prime number.")
    else:
        return("The given number is a prime number.")

if __name__ == "__main__":

    try:
        user_input = int(input("Enter your number:"))
        result = prime_number_finder(user_input)
        print(result)

    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)





#qus 4:

def prime_number(num:int)->bool:
    """this function gives all the prime numbers available between the given two numbers.

        returns:
            Returns the prime numbers between the two numbers."""

    if not isinstance(num,int):
        raise TypeError ("The input should only be an integer.")

    for i in range (2,num):
        if num % i == 0:
            return False
    else:
        return True

if __name__ == "__main__":
    try:
        for i in range(100,201):
            if prime_number(i):
                print(f"{i} is a prime number")
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)





#qus 5:


def factorial_finder(num:int)->int:

    """This function is used to find factorial of a positive number.
    Args:
        num: it should be an int value (num:int)
    Return:
        it return factorial of a number and number should be an int value.
    Raises:
        Value Error: Negative values are not allowed.
        TypeError: Input must be int only."""

    if isinstance (num,bool):
        raise TypeError ("This function not accept bool value")
    if not isinstance (num,int):
        raise TypeError ("Input must be an int only")
    if num<0:
        raise ValueError("Negative values are not allowed")

    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial

if __name__ == "__main__":

    try:
        user_input = int(input("Enter a number here: "))
        result = factorial_finder(user_input)
        print("factorial of",user_input,"is: ",result)

    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print(e)





#qus 6:

def palindrome_finder(text) ->bool:
    """The function identifies whether the given input is a palindrome or not.

    Args:
        Takes a single argument in a string form.

    Returns:
        Returns a boolean value.

    Raises:
        Raises a TypeError if input is not a string.
        Raises a ValueError if the input is only a blank space."""

    if not isinstance(text,str):
        raise TypeError("the input must be string only")
    if text.strip() == "":
        raise ValueError("the must cannot be a blank space")
    else:
        text.strip().lower()

    reverse_text = ""

    for char in text:
        reverse_text = char + reverse_text
    return text == reverse_text

if __name__ == "__main__":
    try:
        user_input = input("Enter the text here:")

        if palindrome_finder(user_input):
            print(f"{user_input} is a palindrome")
        else:
            print(f"{user_input} is not a palindrome")

    except (TypeError,ValueError) as te:
        print("Error: ",te)





#qus 7:

def vowels_count(text:str) ->int:
    """The function counts the number of vowels used in a given word.

    Args:
        Takes one argument in the form of a string.

    Return:
        Returns the sum total of number of times an vowel is used in the string.

    Raises:
        Raises a TypeError if the input is not in string format."""

    if not isinstance(text,str):
        raise TypeError("the input can only be a string.")

    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count = count + 1
    return count

if __name__ == "__main__":
    try:
        user_input = input("Enter your number here:")
        result = vowels_count(user_input)
        print(result)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)





#qus 8:

from typing import List
def second_largest_finder(nums:list[int])->int:
    """finds the second largest available in the given list.

    Parameters:
                nums:list[int]: Alist of integers.

    Returns:
            Returns the second largest unique value available in the list.

    Raises:
            TypeError: if input is not a list.
            ValueError: if list has fewer than two unique elements."""

    if not isinstance(nums,list):
        raise TypeError ("the input must be stored in a list only.")
    if len(nums) < 2:
        raise ValueError("There must be two or more than two elements in the list.")
    if any(not isinstance(current_number,int) for current_number in nums):
        raise TypeError ("All elements must be an integer")

    if numbers_list[0] > numbers_list[1]:
        largest = numbers_list[0]
        second = numbers_list[1]
    else:
        largest = numbers_list[1]
        second = numbers_list[0]

    for current_number in numbers_list[2:]:
        if current_number > largest:
            second = largest
            largest = current_number
        elif current_number != largest and current_number > second:
            second = current_number
    return second

if __name__ == "__main__":

    try:
        numbers_list = [31,5,47,54,87]
        print(second_largest_finder(numbers_list))

    except TypeError as te:
        print(te)

    except ValueError as ve:
        print(ve)

    except Exception as e:
        print(e)





#qus 9:

def digit_sum_finder(n:int)->int:
    """The function calculates the sum of all digits of a given integer.

    Parameter:
                Takes an integer as a input.

    Returns:
            Returns the sum of all digit of an integer.

    Raises:
            TypeError: When the input is not in int form."""

    if not isinstance(n,int):
        raise TypeError("the input must be in integer form only.")


    total = 0
    while n > 0:

        total = total + (n % 10)
        n = n // 10
    return total

if __name__ == "__main__":
    try:
        digit = int(input("enter the number:"))
        result = digit_sum_finder(digit)
        print(result)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)





#qus 10:

from typing import List,Any
def remove_duplicates(List:List[Any])-> List[Any]:
    """Remove duplicates from a list while maintaining orignal order.

    Parameters:
            List (List[Any]): A list containing any type of elements.

    Returns:
            List[Any]: A new list with duplicates removed.

    Raises:
            TypeError: If input is not a List
            ValueError: If the list is empty
    """

    if not isinstance(List,list):
        raise TypeError("Input must only be a list.")
    if len(List) == 0:
        raise ValueError("There must be some value stored in the list.")

    result = []

    for i in List:
        if i not in result:
            result.append(i)
    return result

if __name__ == "__main__":
    try:
        List = [100,40,20,50,20,30,40,100]
        print(remove_duplicates(List))

    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)







