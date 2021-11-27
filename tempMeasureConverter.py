# A program to convert some measurement units including temperatures(F/C)

#Not functioning. Just wanted to get my hands dirty.
import time
print('''Welcome to my unit converter:
Here you can convert many units including Farenheit,Celsius,meters,inch,etc
-----------------------------------------------------------------------
Instructions:
1/Enter your input
2/Enter your input's category(weight,length,temperature)
3/Enter your input's unit:
(Available Conversions:
    Weight: (k)g to (l)bs/(l)bs to (k)g
            
    Length: (i)nch to (m)eter/(m)eter to (i)nch
            (i)nch to (f)eet/(f)eet to (i)nch
            (f)eet to meters/(m)eters to (f)eet
    
    Temperature:    (C)elsius to Kel(v)in/Kel(v)in to (C)elsius
                    (C)elsius to (F)arenheit/(F)arenheit to (C)elsius
            
~~Have fun converting stuff!~~
            ''')

# conversion functions
def itom(a):
    return a
def mtoi(b):
    return b
def ftom(c):
    return c
def mtof(d):
    return d
def ftoi(e):
    return e
def itof(f):
    return f
def ktol(g):
    return g
def ltok(h):
    return h
def ctov(i):
    return i
def vtoc(j):
    return j
def ctof(k):
    return k
def ftoc(l):
    return l
#empty string to put the choice when converting 
choice = ''
#input
try:
    number = int(input("Enter your number to be converted.\n(You will get humiliated if you enter an unacceptable input. Take care :):"))
    print('Acceptable Input!')
    unit = input('''Enter your unit
    Available Units:
    Weight: (k)ilogram,(l)bs
    Length: (i)nch, (m)eter, (f)eet
    Temperature: (C)elsius, Kel(v)in, (F)arenheit
    
    ----Characters inside ( ) are the unit keywords----: :''')
    if unit.lower() == 'k':
        print('You asked to convert the number form kilogram to lbs:The only possible conversion!')
        print('Converting.......')
        time.sleep(2)
        print("The weight in lbs:", ktol(number))
    elif unit.lower() == 'l':
        print('You asked to convert the number form lbs to kilogram:The only possible conversion!')
        print('Converting.......')
        time.sleep(2)
        print("The weight in kilo:", ltok(number))
    elif unit.lower() == 'i':
        choice = input('To which do you want to convert--(m)eter or (f)eet--:').lower()
        if choice == 'm':
            print('Converting to meter')
            time.sleep(2)
            print('The length in meters:', itom(number))
        elif choice == 'f':
            print('Converting to feet....')
            time.sleep(2)
            print('The length in feet:', itof(number))
    elif unit.lower() == 'm':
        choice = input('To which do you want to convert--(i)nch or (f)eet--:').lower()
        if choice == 'i':
            print("Converting to inch...")
            time.sleep(2)
            print('The length in inch:',mtoi(number))
        elif choice == 'f':
            print("Converting to feet...")
            time.sleep(2)
            print("The length in feet:",itof(number))
    elif unit.lower() == 'f':
        choice = input('To which do you want to convert--(m)eter or (i)nch--:').lower()
        if choice == 'm':
            print("Converting to meters...")
            time.sleep(2)
            print("The length in meters:",ftom(number))
        elif choice == 'i':
            print("Converting to inch...")
            time.sleep(2)
            print("The length in inch:",ftoi(number))
    elif unit.lower() == 'c':
        choice = input('To which do you want to convert--Kel(v)in or (f)arenheit--:').lower()
        if choice == 'v':
            print("Converting to Kelvin...")
            time.sleep(2)
            print("The temperature in Kelvin:",ctov(number))
        elif choice == 'f':
            print("Converting to Farenheit...")
            time.sleep(2)
            print("The temperature in Farenheit:",ctof(number))
    elif unit.lower() == 'v':
        choice = input('To which do you want to convert--Kel(v)in or (c)elsius--:').lower()
        if choice == 'v':
            print("Converting to Kelvin...")
            time.sleep(2)
            print("The temperature in Kelvin:",ftoc(number))
        elif choice == 'c':
            print("Converting to Celsius...")
            time.sleep()
            print("The temperature in Celsius:",ctof(number))
    else:
        print("Nope. This operation is not possible!")
        
except:
    print('Enter a number dumbass!')
    quit()

            
            
            
        
    
