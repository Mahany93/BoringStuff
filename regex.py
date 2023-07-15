# Find phone number without regular expression.

""" def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal:
            return False
        if text[3] != '-':
            return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a Phone number? ')
print(isPhoneNumber('415-555-4242')) """
################################################################################################

# Achieve the same Goal as the above function using Regular Expressions.

import re
""" phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
areaCode, mainNum= mo.groups()
print('Phone Number Found: ' + mo.group())
print('Area Code is: ' + areaCode)
print('Main Number is: ' + mainNum)
print(mo.group(1))
print(mo.group(2))
print(mo.group(0)) """

########## Matching Multiple Groups with Pipe ##########
""" heroRegex= re.compile(r'Batman|Tina Fey')
mo1= heroRegex.search('Batman and Tina Fey')
mo2= heroRegex.search('Tina Fey and Batman')
mo3 = heroRegex.findall('Batman and Tina Fey')
print(mo1.group())
print(mo2.group())
print(mo3)
 """

########## Optional Matching with the Question Mark ##########
""" batRegex= re.compile(r'Bat(man|mobile|copter|bat)')
batRegex2= re.compile(r'Bat(wo)?man')
mo = batRegex.search('Batmobile lost a wheel')
mo2 = batRegex2.search('Batwoman lost a wheel')
print(mo2.group())
 """

########## Matching Zero or More with the Star ##########
""" batRegex= re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowowowowowoman')
print(mo.group())
print(mo2.group())
print(mo3.group())
 """

########## Matching One or More with the Plus ##########
batRegex= re.compile(r'Bat(wo)+man', re.I)
mo = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of BATWOMAN')
mo3 = batRegex.search('The Adventures of Batwowowowowowowowoman')
print(mo == None)
print(mo2.group())
print(mo3.group())


########## Matching Specific Repetitions with Braces ##########
# haRegex = re.compile(r'(Ha){3}')
# mo = haRegex.search('HaHaHa')
# mo2 = haRegex.search('HaHa')
# print(mo.group())
# print(mo2 == None)