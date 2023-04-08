#(2_1-2_2) assign a message to a variable, and then print that message. 
#Then change the value of the variable to a new message, and print the new message.
message = "this is a message"

print(f"\n\t{message.title()}")

message = "this no longer is a message"

print(f"\n\t\t{message.upper()}")

# fstring - f""  ---  for both variables and text
# methods - upper, lower, title. --- change the casing for text inside a variable(strings and lists so far)

# 2-4 Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name = "KArl MArX"
print(name.title())
print(name.upper())
print(name.lower())

#Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
# Then compose your message and represent it with a new variable called message. Print your message

famous_person = "Thomas Sankara"

message = f"{famous_person.title()} once said 'peepeepoopoo'"

print(message)

# methods - strip, lstrip, rstrip --- clear up whitespace from variables
# whitespace - \t, \n --- tab and newline
#2-7

persons_name = " Che Guevara   "

print(persons_name)

print(f"\n\t{persons_name.lstrip()}")
print(f"\n\t{persons_name.rstrip()}")
print(f"\n\t{persons_name.strip()}")

# lists - work the same as strings but multiple values, starts at 0 and uses brackets [].

examplelist = ["1", 5, "Panther"]
print(examplelist[1])

# modifying lists - change a value same as strings

examplelist[1] = "five"
print(examplelist[1])

# method - append() adds value to the end of the list
examplelist.append("new value1")
print(examplelist)
#>>>['1', 'five', 'Panther', 'new value1'] (">>> means console output")


# method - insert() adds value at any position in the list(pushes the value at the position and subsequent values to the right or +1)
# you write the position then comma+space then value --- insert(0, "value")

# putting this in the middle so the output should be 
#>>>['1', 'five', 'new value2','Panther', 'new value1']
examplelist.insert(2, "new value2")
print(examplelist)
#>>>['1', 'five', 'new value2','Panther', 'new value1']


# statement - del remove value in any position
del examplelist[3]
print(examplelist)
#>>>['1', 'five', 'new value2', 'new value1']

# method - pop() removes value but assigns it to a new variable. Empty parentheses() = last item in a list
lastvalue = examplelist.pop()
print(examplelist)
print(lastvalue)
#>>>['1', 'five', 'new value2']
#>>>new value1

examplelist.append(lastvalue)
# reset list to earlier state - IGNORE
#>>>['1', 'five', 'new value2', 'new value1']


# method - pop() remove value by position
listvalue1 = examplelist.pop(1)
print(examplelist)
print(listvalue1)


# reset list to earlier state - IGNORE
examplelist.insert(1, listvalue1)
#>>>['1', 'five', 'new value2', 'new value1']


# method - remove() removes value by value(if u dont know position of value on list but know said value)

examplelist.remove("new value2")
#>>>['1', 'five', 'new value1']
examplelist.insert(2, "new value2")

# organizing a list

countries = ["tExas", "aUStraliA", "cANaDa", "cALIfORnia", "bRAzil"]

# function - sorted() display list in alphabetical order without affecting the actual list

print(countries)
print(f"\n\t{sorted(countries)}")
#>>>['tExas', 'aUStraliA', 'cANaDa', 'cALIfORnia', 'bRAzil']
#>>>['aUStraliA', 'bRAzil', 'cALIfORnia', 'cANaDa', 'tExas']

# sorted() can be reverasable with reverse=True

print(f"\n\t{sorted(countries, reverse=True)}")
#>>>['tExas', 'cANaDa', 'cALIfORnia', 'bRAzil', 'aUStraliA']

# method - reverse() simply reverses the order of the list 

countries.reverse()
print(f"\n\t{countries}")
#>>>['bRAzil', 'cALIfORnia', 'cANaDa', 'aUStraliA', 'tExas']

# use reverse again to reset the list to its original order
countries.reverse()
print(f"\n\t{countries}")
#>>>['tExas', 'aUStraliA', 'cANaDa', 'cALIfORnia', 'bRAzil']

# method - sort() list alphabetically permanently

countries.sort()
print(f"\n\t{countries}")
#>>>['aUStraliA', 'bRAzil', 'cALIfORnia', 'cANaDa', 'tExas']

#can be reversable with reverse=True
countries.sort(reverse=True)
print(f"\n\t{countries}")
#['tExas', 'cANaDa', 'cALIfORnia', 'bRAzil', 'aUStraliA']

# function - len() find out the lenght of a list(amount of values)
print(len(countries))
#>>>5





