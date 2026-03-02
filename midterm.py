def is_valid_url(url):
    """
    This function checks if a URL is valid.
    A valid URL:
    - starts with http:// or https://
    - contains at least one dot
    - contains no spaces
    """
    url = str(url)
# The URL must start correctly
    if url[:7] == "http://" or url[:8] == "https://":

        # It must contain a dot
        if "." in url:

            # It should not have any spaces
            if " " not in url:
                return True

    return False

print(is_valid_url("https://github.com"))
print(is_valid_url("hello"))


#### Ex 2

def longest_word(filename):
    """
    This function returns the longest word in a text file.
    :param filename:
    :return:
    """
    f = open(filename, "r")
    longest = ""
    for line in f:
        words = line.split()
        for word in words:
            if word[:2] == "un":
                if len(word) > len(longest):
                    longest = word
    f.close()
    return longest

print(longest_word("ex2.txt"))

## Ex 3

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("2704702208931031198668911301398022074072"))
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("4257304920394478392772938744930294037524"))


## Ex 4: What will be the value of "a" at the end of the code:

a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

## Ex 5

import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        random_numbers[i] = "XX"

print(random_numbers)

## Ex 6
print(8 // 3 + 2 * 4)

# Ex 7

# We can add elements to the list.
a = [1, 2, 3]
a.append("John")
a.append("Doe")
print(a)

# We can also substitute an object by another element

a = [True, [1, "Bob", -5.3], False, "Spain", 38.97]
print(a[2])
a [2] = "No longer False!"
print(a)

#word = "cat"
#word[0] = "b"

## Ex 8

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

## Ex 9

def days_since_birthday(birthday):
    """
    birthday format: DD-MM-YYYY
    returns number of days from full years only
    """
    parts = birthday.split("-")
    birth_year = int(parts[2])
    current_year = 2026
    total_days = 0
    for year in range(birth_year + 1, current_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366
        else:
            total_days += 365
    return total_days

print(days_since_birthday("16-02-2006"))


