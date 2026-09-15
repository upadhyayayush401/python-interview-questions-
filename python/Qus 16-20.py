


#qus 16:


def power_finder(num1:int, power:int) ->int:
    """The function calculates the power value of num1 as compared to num2.

    Parameters:
                Takes two inputs as a number and a power in form of int.

    Returns:
            Returns the calculated power value of the number.

    Raises:
            TypeError: when the given input is not in integer form.
            ValueError: when the given input is 0 or negative integer.
    """

    if not isinstance(num1,int) or not isinstance(num1,int):
        raise TypeError("the given value must be integer")

    if num1 == 0 and power == 0:
        raise ValueError("the given value cannot be zero")


    result = 1
    for i in range(power):
        result = result * num1
    return result

if __name__ == "__main__":

    try:
        num1 = int(input("Enter the base value: "))
        power = int(input("Enter the power value"))
        print(power_finder(num1,power))

    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)




#qus 17:


def even_number_finder(num:int)->list:
    """The function finds out if the number is in the range of given input and whether it is even or not and adds it in a list
    Parameters:
                Takes input in form of integer.
    Return:
            Returns the list of even numbers in the range of given input.
    Raises:
            TypeError: When the input is not in form of integer.
            ValueError: When the input is zero or blank.
    """
    if not isinstance(num,int):
        raise TypeError("The input must be int")
    if num == 0 or num == "":
        raise ValueError("The input cannot be zero or blank.")

    list1 = []
    for i in range(1,num+1):
        if i % 2 == 0:
            list1.append(i)
    return list1

if __name__ == "__main__":

    try:
        num = int(input("Enter the number: "))
        print(even_number_finder(num))

    except TypeError as te:
        print(te)

    except ValueError as ve:
        print(ve)

    except Exception as e:
        print(e)




#qus 18:



def binary_finder(sorted_list:list,target:int) -> int:
    """The function finds the index of the given target using binary method.

    Parameters:
                sorted_list:Takes input in form of a list.
                target: Takes input in form of integer.

    Returns:
            Returns the index of the given target in the target variable.

    Raises:
            TypeError: When the given input is not in the form of a list or int.
    """

    if not isinstance (sorted_list,list):
        raise TypeError ("The sorted_list must be a list.")
    if not isinstance (target,int):
        raise ValueError ("The target must be in integer form.")

    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high)//2
        if sorted_list[mid] == target:
            return (mid)

        elif target < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid +1
    else:
        return(-1)

if __name__ == "__main__":

    try:
        sorted_list = [21, 23, 28, 37, 43, 46, 54, 57, 68, 75, 90]
        result = binary_finder(sorted_list,54)
        print(result)
    except TypeError as te:
        print(te)



#qus 19:



def reverse_sentence(text:str)->str:
    """The function reverses the words of the given sentence and gives the resultant as output.

    Parameters:
                takes a string as a input.

    Returns:
            Returns the reverse of the given text.

    Raises: 
            TypeError: When the given input is not in form of a string.
            ValueError: When the input is blank or a whitespace only.
    """

    if not isinstance(text,str):
        raise TypeError("The text must be a string.")
    if text == "" :
        raise ValueError ("The input cannot be blank")

    words_list = []
    words = ""
    rev_sentence = ""

    for char in text:
        if char != " ":
            words = words + char

        else:
            words_list.append(words)
            words = ""
    words_list.append(words)


    for i in range (len(words_list)-1,-1,-1):
        rev_sentence = rev_sentence + words_list[i]
        if i != 0:
            rev_sentence = rev_sentence + " "
    return(rev_sentence)

if __name__ == "__main__":
    try:
        text = input("Enter you text here: ")
        print(reverse_sentence(text))
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)



#qus 20:


def gcd_finder(n1:int,n2:int)->int:
    """The function calculates the greatest common divisor between two numbers.

    Parameters:
                Takes input in the form of integer.

    Returns:
            returns the greatest common divisor.

    Raises:
            TypeError: When the given input is not an integer.
            ValueError: When the input is 0 or blank
    """

    if not isinstance(n1,int):
        raise TypeError("The numbers must be an integer.")
    if not isinstance(n1,int):
        raise TypeError("The numbers must be an integer.")
    if n1 == 0 or n2 == 0:
        raise ValueError ("The input cannot be zero or blank.")

    list1 = []
    for n in range (1,n2+1):
        if n1 % n == 0 and n2 % n == 0:
            list1.append(n)
    return list1[-1]

if __name__ == "__main__":
    try:
        n1 = int(input("Enter the first number:"))
        n2 = int(input("Enter the second number:"))
        print(gcd_finder(n1,n2))

    except (TypeError,ValueError) as te:
        print(te)

    except Exception as e:
        print(e)


