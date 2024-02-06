"""
DESCRIPTION:
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""


import string


def find_missing_letter(arr):
    mi_ind = string.ascii_letters.find(arr[0])
    ma_ind = string.ascii_letters.find(arr[-1])

    strng = string.ascii_letters[mi_ind:ma_ind +1]

    for let in strng:
        if let not in arr:
            let = string.ascii_letters.find(let)
            return string.ascii_letters[let]


print(find_missing_letter(['b','d']))

