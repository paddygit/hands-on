# if statement

x = 5
if x < 10:
    print('Smaller')
if x > 10:
    print('Bigger')

print('Done')

# Discuss Nested if

x = 20
if x < 10:
    print('Smaller')
elif x < 20:
    print('Bigger')
else:
    print('Too big!')

# else can be optional.. but else is a catch all which will not be present

# order mateers. first positive is executed

x = 9
if x < 20:
    print('Small')
elif x < 10:
    print('Smaller')
else:
    print('Big!')
