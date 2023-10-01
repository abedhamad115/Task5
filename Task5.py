#Q1
print('::::::::: Question 1 :::::::::')
name = input("name: ")
age = (input("age: "))
st = input("street: ")
city = input("city: ")
country = input("country: ")
#Q2
print('::::::::: Question 2 :::::::::')
print (f'"name: {name}"')
print (f'"age: {age}"')
print (f'"address: {st},{city},{country}"')
input('press enter to contenue...')
#Q3
print('::::::::: Question 3 :::::::::')
print (f'"Hello {name}, your age is {int(age)-5} years old, your address is {st}, {city}, {country}."')
input('press enter to contenue...')
#Q4
print('::::::::: Question 4 :::::::::')
print ('name',type(name))
print ('age',type(age))
print ('st',type(st))
print ('city',type(city))
print('country',type(country))
input('press enter to contenue...')
#Q5
print('::::::::: Question 5 :::::::::')
print (f'"Hello {name}, How Are You? \ """ Your Age Is "{int(age)-5}"" + And Your Country Is: {country}')
input('press enter to contenue...')
#Q6
print('::::::::: Question 6 :::::::::')
print (f'''"Hello {name}, How Are You? \ 
       """ Your Age Is "{int(age)-5}"" + 
       And Your City Is: {city}''')
input('press enter to contenue...')
#Q7
print('::::::::: Question 7 :::::::::')
name = 'ITF Gsg Python'
print ('First letter is', '"',name[0],'"')
print ('Third letter is', '"',name[2],'"')
print ('Last letter is', '"',name[-1],'"')
input('press enter to contenue...')
#Q8
print('::::::::: Question 8 :::::::::')
print (name[11:])
print (name[0:2])
print (name[0:7:2])
print (name[:7:-1])
input('press enter to contenue...')
#Q9
print('::::::::: Question 9 :::::::::')
name = "$&$&Mohammed$&$&"
print (name.strip('$&'))
input('press enter to contenue...')
#Q10
print('::::::::: Question 10 :::::::::')
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print (msg.replace('%7', 'love'))
input('press enter to contenue...')
#Q11
print('::::::::: Question 11 :::::::::')
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print (num1.zfill(5))
print (num2.zfill(5))
print (num3.zfill(5))
print (num4.zfill(5))
print (num5.zfill(5))
print (num6.zfill(5))
input('press enter to contenue...')
#Q13
print('::::::::: Question 13 :::::::::')
name = 'abed HAMAD'
print ('''in title the first latter from evry word become capital latter, and other letters become small,
but in capitalize just the first latter in the sentance will become capital,and other letters become small''')
print ('for example: ',name)
print ('name in tltle:',name.title())
print ('name in capitalize:',name.capitalize())
input('press enter to contenue...')
#Q14
print('::::::::: Question 14 :::::::::')
first_name='Dana'
print(f'''
**********{first_name}
**********{first_name}**********
{first_name}**********''')
input('press enter to contenue...')
#Q15
print('::::::::: Question 15 :::::::::')
name_one = "SaMER"
name_two = "Abed"
print (name_one.swapcase())
print (name_two.swapcase())
print (name_one.lower())
print (name_two.upper())
input('press enter to contenue...')
#Q16
print('::::::::: Question 16 :::::::::')
print ('is name_one contains only upper case letters?', name_one.isupper())
print ('is name_two contains only lower case letters?', name_one.isupper())
input('press enter to contenue...')
#Q17
print('::::::::: Question 17 :::::::::')
print('is the first latter of name_one is "S"?',name_one[0].startswith('S'))
print('is the last two letters of name_two is "HD"?',name_two[-1:-2].endswith('HD'))
input('press enter to contenue...')
#Q18
print('::::::::: Question 18 :::::::::')
msg = "I Love Python And Although I Love GSG with Zakaria"
print('how many times the word "love" was printed?',msg.count("Love"))
print('how many times the letter "t" was printed?',msg.count("t"))
input('press enter to contenue...')
#Q19
print('::::::::: Question 19 :::::::::')
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print (msg.replace('%7', 'love',1))
input('press enter to contenue...')
#Q20
print('::::::::: Question 20 :::::::::')
test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"
test1rev = test1[::-1]
test2rev = test2[::-1]
test3rev = test3[::-1]
test4rev = test4[::-1]
if test1.lower() == test1rev.lower():
    print(test1, ' is palindrome')
else:
    print(test1,' is not palindrome')
if test2.lower() == test2rev.lower():
    print(test2,' is palindrome')
else:
    print(test2,' is not palindrome')
if test3.strip(".").replace(" ","").lower() == test3rev.strip(".").replace(" ","").lower():
    print(test3,' is palindrome')
else:
    print(test3,' is not palindrome')
if test4.lower() == test4rev.lower():
    print(test4,' is palindrome')
else:
    print(test4,' is not palindrome')
# symmetry
test3new = test3.strip(".").replace(" ","").lower()
size1=len(test1)
size2=len(test2)
size3=len(test3new)
size4=len(test4)

if size1%2==0:
    h1=size1//2
    if test1[0:h1]==test1[h1:size1]:
        print(test1,' is symmetric')
    else:
         print(test1, ' is not symmetric')
else:
     print(test1,' is not symmetric')

if size2%2==0:
    h2=size2//2
    if test2[0:h2]==test2[h2:size2]:
        print(test2,' is symmetric')
    else:
        print(test2, ' is not symmetric')
else:
     print(test2,' is not symmetric')

if size3%2==0:
    h3=size3//2
    if test3new[0:h3]==test3new[h3:size3]:
        print(test3,' is symmetric')
    else:
        print(test3, ' is not symmetric')
else:
     print(test3,' is not symmetric')

if size4%2==0:
    h4=size4//2
    if test4[0:h4]==test4[h4:size4]:
        print(test4,' is symmetric')
    else:
        print(test4, ' is not symmetric')
else:
     print(test4,' is not symmetric')

print(':::::::::::: THANK YOU ::::::::::::')