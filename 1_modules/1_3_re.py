# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.3: Os Module in Python 
# python 1_3_re.py
blank = "----------------------"

import re
# Regular Expression Module
# A regular expression (or RE) specifies a set of strings that matches it; the functions in this module 
# let you check if a particular string matches a given regular expression.
# (or if a given regular expression matches a particular string, which comes down to the same thing)

# Find all
str = "Let me keep us alive | In their forgetful minds"
find_all = re.findall("alive", str)
print(find_all)
print(blank)

# Split
split = re.split("minds", str)
print(split)
print(blank)

# Sub
sub = re.sub(" ", "|", str)
# sub = re.sub("\s", "|", str)
print(sub)
print(blank)

# Search
search = re.search("forgetful", str)
span = search.span()
# start = search.start()
# end = search.end()
# group = search.group()
# strin = search.string

print(search)
print(f"Target located at {span}")
print(blank)

##############################################################################################################

# Searching character via range

"""
    [] - All the characters that written inside square brackets will be searched.
    
    [abc]  => a      : 1 match   
              ac     : 2 matches
              Python : No matches
    
    [a-e]  => [abcde]
    [1-5]  => [12345]
    [0-39] => [01239]

    [^abc]  => Characters outside of abc
    [^0-9]  => Non-digit characters

"""

search_1 = re.findall("[abc]", str)
print(f"search_1: {search_1}")
print(blank)

search_2 = re.findall("[clock]", str)
print(f"search_2: {search_2}")
print(blank)

search_3 = re.findall("[a-e]", str)
print(f"search_3: {search_3}")
print(blank)

search_4 = re.findall("[^a-e]", str)
print(f"search_4: {search_4}")
print(blank)

##############################################################################################################

# Searching character via range - 2
 
"""
    . - Denotes any character

        .. => a      : No matches 
              ab     : 1 match
              ab     : 1 match
              ab     : 2 matches

"""
search_5 = re.findall("...", str)
print(f"search_5: {search_5}")
print(blank)

search_6 = re.findall("for...ful", str)
print(f"search_6: {search_6}")
print(blank)

##############################################################################################################

# Searching character via range - 3

"""
    ^ - Does the input start with the stated characters ?

        ^a => a      : 1 match 
              abc    : 1 match
              bac    : No matches 

"""
search_7 = re.findall("^L", str)
print(f"search_7: {search_7}")
print(blank)

##############################################################################################################

# Searching character via range - 4

"""
    $ - Does the input end with the stated characters ?

        a$ => a      : 1 match 
              lambda : 1 match
              Python : No matches 

"""

search_8 = re.findall("s$", str)
print(f"search_8: {search_8}")
print(blank)

search_9 = re.findall("minds$", str)
print(f"search_9: {search_9}")
print(blank)

##############################################################################################################

# Searching character via range - 5

"""
    * - Checks the characters to be zero or more.

        ma*n => mn   : 1 match 
                man  : 1 match
                maan : 1 match
                main : No matches - because n is not after a

"""

search_10 = re.findall("ke*p", str)
print(f"search_10: {search_10}")
print(blank)

##############################################################################################################

# Searching character via range - 6

"""
    + - Checks the characters to be one or more.

        ma+n => mn   : No matches
                man  : 1 match
                maan : 1 match
                main : No matches - because n is not after a

"""

search_11 = re.findall("ke+p", str)
print(f"search_11: {search_1}")
print(blank)

##############################################################################################################

# Searching character via range - 7

"""
    ? - Checks the characters to be zero or one.

        ma?n => mn   : No matches
                man  : 1 match
                maan : 1 match
                main : No matches - because n is not after a

"""

search_12 = re.findall("ke?p", str)
print(f"search_12: {search_12}")
print(blank)

##############################################################################################################

# Searching character via range - 8

"""
    {} - Checks character size.

        al{2}       => character 'l' must be repeated after 'a' two times
        al{2,3}     => character 'l' must be repeated after 'a' at least two times, at most 3 times
        [0-9]{2,4}  => at least 2 at most 4 digit numbers

"""

search_13 = re.findall("e{2}", str)
# search_13 = re.findall("e{2,3}", str)
# search_13 = re.findall("[0,9]", str)
print(f"search_13: {search_13}")
print(blank)

##############################################################################################################

# Searching character via range - 9

"""
    | - One of the alternatives must be occur.

        a|b => a or b
        cde    : No matches
        ade    : 1 match
        acdbea : 3 matches

"""

##############################################################################################################

# Searching character via range - 10

"""
    () - Used for grouping

        (a|b|c)xz => xz must be placed between characters a,b and c

"""

##############################################################################################################

# Searching character via range - 11

"""
    \ - Allows search for special characters

        /$a => Searchs '$' character after character 'a'

    \A - Is the specified character at the beginning of the string?
        \Athe => Is 'the' at the beginning of the string?

    \Z - Is the specified character at the end of the string?
        the\Z => Is 'the' at the end of the string?

    \b - Is the specified character at the end or beginning of the string?
        \bthe => Is 'the' at the beginning of the string?
        the\b => Is 'the' at the end of the string?

    \B - Is the specified character not at the end or beginning of the string?
        \Bthe => Is 'the' not at the beginning of the string?
        the\B => Is 'the' not at the end of the string?

    \d - Searchs for numbers, digits.
        \d => 12abc34

    \D - Searchs for non-digits.
        \D => 1ab44_50
    
    \s - Searchs for spaces.
    \S - Searchs for out of spaces.
    \w - Alphabetical characters, numbers and downstroke.
    \W - Opposite of \w
"""
