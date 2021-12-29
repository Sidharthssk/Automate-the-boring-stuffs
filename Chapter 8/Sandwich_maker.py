import pyinputplus as pyip

bread_type = pyip.inputMenu(['Wheat','White','sourdough'])

protein_type = pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'])

Cheese_requirement=pyip.inputYesNo('Do yo want cheese or not')

if Cheese_requirement == 'yes':
    cheese_type=pyip.inputMenu(['Cheddar','Swiss','Mozzarella'])

mayo_requirement=pyip.inputYesNo('Do yo want mayo or not')
mustard_requirement=pyip.inputYesNo('Do yo want Mustard or not')
lettuce_requirement = pyip.inputYesNo('Do yo want lettuce or not')
tomato_requirement = pyip.inputYesNo('Do yo want tomato or not')

sandwich_number = pyip.inputInt('Enter the number of sandwiches required',min=1)

total = 0
if bread_type == 'Wheat':
    total+=4
elif bread_type == 'White':
    total+=3
else:
    total+=5

if protein_type == 'Chicken':
    total+=10
elif protein_type == 'Turkey':
    total+=15
elif protein_type == 'Ham':
    total+=25
else:
    total+=20

if cheese_type == 'Cheddar':
    total+=20
elif cheese_type == 'Swiss':
    total+=15
else:
    total+=20

if mayo_requirement == 'yes':
    total+=10
if mustard_requirement == 'yes':
    total+=1
if lettuce_requirement == 'yes':
    total+=5
if tomato_requirement == 'yes':
    total+=3

print('Your total cost is '+str(sandwich_number*total))