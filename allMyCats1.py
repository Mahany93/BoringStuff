myCats = []

while True:
    print('Please enter the name of cat number ' + str(len(myCats) + 1) + ' (or enter nothing to stop.):')
    catName = input()
    if catName == '':
        break
    myCats = myCats + [catName]
print('My cat names are: ')
for name in myCats:
    print(' ' + name)