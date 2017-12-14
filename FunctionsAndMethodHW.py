# coding: utf-8

# # Functions and Methods Homework
#
# Complete the following questions:
# ____
# **Write a function that computes the volume of a sphere given its radius.**

# In[48]:


def vol(rad):
    return (4 / 3) * 3.14 * rad ** 3


print(vol(2))


# ___
# **Write a function that checks whether a number is in a given range (Inclusive of high and low)**

# In[47]:


def ran_check(num, low, high):
    if num in range(low, high + 1):
        return "Number is in range"
    else:
        return "Number is not in range"


print(ran_check(10, 1, 8))


# If you only wanted to return a boolean:

# In[45]:


def ran_bool(num, low, high):
    if num in range(low, high + 1):
        return True
    else:
        return False


# In[46]:


print(ran_bool(3, 1, 10))

# ____
# **Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.**
#
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output :
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33
#
# If you feel ambitious, explore the Collections module to solve this problem!

# In[41]:


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
s.split()


def up_low(s):
    lower = 0
    upper = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Expected Output:")
    print("No. of Upper case characters :" + str(upper))
    print("No. of Lower case characters :" + str(lower))

print(up_low(s))


# ____
# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
#
#     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#     Unique List : [1, 2, 3, 4, 5]

# In[50]:


def unique_list(l):
    newList = []
    for item in l:
        if item not in newList:
            newList.append(item)
    return newList


# In[51]:


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# ____
# **Write a Python function to multiply all the numbers in a list.**
#
#     Sample List : [1, 2, 3, -4]
#     Expected Output : -24

# In[52]:


def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res


# In[53]:


print(multiply([1, 2, 3, -4]))


# ____
# **Write a Python function that checks whether a passed string is palindrome or not.**
#
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# In[56]:


def palindrome(s):
    s1 = s[::-1]
    if s == s1:
        return True
    else:
        return False


# In[57]:


print(palindrome('hanah'))

# ____
# **Hard**:
#
# Write a Python function to check whether a string is pangram or not.
#
#     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#     For example : "The quick brown fox jumps over the lazy dog"
#
# Hint: Look at the string module

# In[106]:


import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    result = True
    for letter in alphabet:
        if letter not in str1:
            result = False
            break
    return result


print(ispangram("pack my box with five dozen liquor jugs"))




# ####**Great Job!**
