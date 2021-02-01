def c2f(c):
    f=c*1.8+32
    return round(f,2)

def f2c(f):
    c=(f-32)/1.8
    return round(c,2)

def m2mile(input):
    return round(input/1609.34,2)

def m2foot(m):
    foot=m*1.0936
    return round(foot,2)

def m2inch(m):
    inch=m*39.37
    return round (inch,2)

def foot2m(foot):
    m=foot/1.0936
    return round(m,2)

def inch2m(inch):
    m=inch/39.37
    return round(m,2)
def mile2m(input):
    return round(input*1609.34,2)

def kg2pound(input):
    return round(input*2.2064,2)
def g2pound(input):
    return round(input/1000*2.2064,2)

def pound2kg(input):
    return round(input/2.2064,2)
def pound2g(input):
    return round(input*1000/2.2064,2)

def kg2ounce(input):
    return round(input*35.274,2)
def g2ounce(input):
    return round(input*35.274,2/1000)

def ounce2kg(input):
    return round(input/35.274,2)
def ounce2g(input):
    return round(input/35.274,2*1000)





def filter(input):
    list1=input.lower()
    list1=list1.split()
    output=[]
    for item in list1:
        temp=isIn(item)
        if temp!=None:
            output.append(temp)
    return output


def isIn(string):
    list=['foot','inch','mile','meter','ounce','pound','kilogram','gram']
    try:
        return float(string)
    except:
        for item in list:
            if item in string:
                return item
        if 'k'in string and 'g'in string:
            return 'kilogram'
        if 'g'==string:
            return 'gram'
        if 'c'==string:
            return 'c'
        if 'f'==string:
            return 'f'

def check_validation(list):
    number_counter=0;
    string_counter=0;
    num_pos=0;
    for item in list:
        if type(item)==type("fsafaf"):
            string_counter+=1
        elif type(item)==type(100.0):
            number_counter+=1
        else:
            pass
    for item in list:
        if type(item)==type(1.0):
            break;
        else:
            num_pos+=1




    if(number_counter==1 and string_counter==2 and num_pos!=2):
        return num_pos
    else:
        return 10086

def converter(value,string1,string2):
    if string1==string2:
        return value
    elif string1=='c'and string2=='f':
        return c2f(value)
    elif string1=='f'and string2=='c':
        return f2c

    elif string1=='meter'and string2=='foot':
        return m2foot(value)
    elif string1=='meter'and string2=='inch':
        return m2inch(value)
    elif string1=='meter'and string2=='mile':
        return m2mile(value)


    elif string1=='mile'and string2=='meter':
        return mile2m(value)
    elif string1=='foot'and string2=='meter':
        return foot2m(value)
    elif string1=='inch'and string2=='meter':
        return inch2m(value)

    elif string1=='kilogram'and string2=='ounce':
        return kg2ounce(value)
    elif string1=='kilogram'and string2=='pound':
        return kg2pound(value)
    elif string1=='pound'and string2=='kilogram':
        return pound2kg(value)
    elif string1=='ounce'and string2=='kilogram':
        return ounce2kg(value)

    elif string1=='gram'and string2=='ounce':
        return g2ounce(value)
    elif string1=='gram'and string2=='pound':
        return g2pound(value)
    elif string1=='pound'and string2=='gram':
        return pound2g(value)
    elif string1=='ounce'and string2=='gram':
        return ounce2g(value)


print("Wlecome to use YZL converter 2.0 edition")


while True:
    while True:
        print("Please enter your instruction:")
        filtedtext=filter(input())
        num_pos=check_validation(filtedtext)
        if num_pos==10086:
            print("Invalid input, try again. ")
        else:
            break
    value=filtedtext[num_pos]
    string1=filtedtext[num_pos+1]
    filtedtext.remove(value)
    filtedtext.remove(string1)
    string2=filtedtext[0]

    answer=converter(value,string1,string2)
    if answer==None:
        print("We do not provide this convert service.")
    else:
        print("The answer is:",answer,string2)
        print("Do you have other things to convert?y/n")
        temp=input()
        temp=temp.lower()
        if 'n' in temp:
            break

print("Thanks for using my converter, there is also a GUI edition which is easier to use ：)")





