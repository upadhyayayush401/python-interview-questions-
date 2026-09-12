


#qus 11:

def recursion_factorial(num:int)->int:
    """The function calculates the factorial of given input while limiting the recursion.

    Args:
            Takes an input argument in the form of integer.

    Returns:
            Returns the factorial of the given integer.

    Raises:
            TypeError: When the data type is not an integer.
            ValueError: when the input is zero or nill"""

    if not isinstance(num,int):
        raise TypeError("the input must be integer only.")
    if num == 0 or num == "":
        raise ValueError("There must be given a valid input.")

    if num == 0 or num == 1:
        return 1
    return num * recursion_factorial(num-1)


if __name__ == "__main__":

    try:
        user_input = int(input("Enter your number here: "))
        print(recursion_factorial(user_input))

    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)



# In[6]:


#qus 12:


def count_string(text:str) ->dict:
    """The function counts every single character in a given string.

    Parameters:
                Takes an input in form of a string.

    Return:
            Returns the key-value pair as character and count in form of dictionary.

    Raises:
            TypeError: When the input value is not string.
            ValueError: When the input is blank or whitespace"""

    if not isinstance(text,str):
        raise TypeError("The input must be string only.")
    if text == " ":
        raise ValueError("The input cannot be blank.")

    count = {}

    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

if __name__ == "__main__":
    try:
        user_input = input("Enter your text here: ")
        print(count_string(user_input))

    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)


# In[8]:


#qus 13:


def anagram(string1:str, string2:str)->bool:
    """check whether two strings are anagrams using character counting

    Parameters:
                string1 :first input string.
                string2 : dsecond input string.

    Returns:
            Boolean : True if strings are anagrams.
    """

    if not isinstance(string1,str) or not isinstance(string2,str):
        raise TypeError("The input must be string only.")

    string1 = string1.replace(" ","").lower()
    string2 = string2.replace(" ","").lower()

    if len(string1) != len(string2):
        return(False)
    else:
        for char in string1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in string2:
            if char not in count:
                return(False)
                break
            count[char] -= 1
            if count[char] < 0:
                return(False)
                break
        else:
            return(True)

if __name__ == "__main__":
    try:
        string1 = "abcdef"
        string2 = "abcdef"
        result = anagram(string1,string2)
        print(result)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)


# In[11]:


#qus 14:

def fibonacci(n:int) -> list:

    """The function calculates the fibonacci sequence from 0 to n.

    Parameters:
                take input as n in the form of integer.

    Return:
            Fibonacci sequence for the given number.


    Raises:
            TypeError: If the given input is in another form than integer.

            ValueEroor: If the given input is less than 0.
    """

    if not isinstance(n,int):
        raise TypeError("The given input must be a integer.")

    if n < 0:
        raise ValueError("The given input must be a positive integer.")

    if n == 0:
        return []

    if n == 1:
        return [1]

    else:
        list1 = [0,1]

        for n in range(2,n):
            nextterm = list1[-1] + list1[-2]
            list1.append(nextterm)
    return list1

if __name__ == "__main__":
    try:
        n = int(input("Enter your number: "))
        print (fibonacci(9))
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)


# In[ ]:


#qus 15:

def leap_year_finder(num:int) -> bool:


    """The function finds if the given year is a leap year or not.
    Parameters:
                Takes input as year in form of a integer.
    Returns:
            Returns if the year is leap year or not in form of a boolean value.
    Raises:
            TypeError: When the gicven input is not in form of integer.
            ValueError: When the given input is not more than 3 numbers.
    """

    if not isinstance(num,int):
        raise TypeError("Input must be a string value.")
    if num < 1000:
        raise ValueError("Input must be in thousands.")


    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        inp = int(input("Enter the year here: "))
        print(leap_year_finder(inp))
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)


# In[ ]:




