

def c2f(c):
    f=c*1.8+32
    return round(f,2)

def f2c(f):
    c=(f-32)/1.8
    return round(c,2)

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

first_choice=0
second_choice=0
input_value=0.0
output_value=0.0
flag=1
print("Welcome use YunzeLian's converter, console edition")
print("Please following the instruction and enter a right number")

while flag==1:
    print("Please enter the value needed to be converted")
    input_value=float(input())

    print("What do you want to convert FROM ?")
    print("1.Meter  2.Foot  3.Inch  4.F  5C")
    first_choice=int(input())
    if first_choice==1:
        print("What do you want to convert TO ?")
        print("1.Foot 2.Inch")
        second_choice=int(input())
        if second_choice==1:
            output_value=m2foot(input_value)
            print("\n",input_value,"meters equal to",output_value,"foots.\n")
        else:
            output_value=m2inch(input_value)
            print("\n",input_value,"meters equal to",output_value,"inchs.\n")
        
    elif first_choice==2:
        output_value=foot2m(input_value)
        print("\n",input_value,"foots equal to",output_value,"meters.\n")

    elif first_choice==3:
        output_value=inch2m(input_value)
        print("\n",input_value,"inchs equal to",output_value," meters.\n")
    elif first_choice==4:
        output_value=f2c(input_value)
        print("\n",input_value,"F equal to",output_value,"C.\n")
    elif first_choice==5:
        output_value=c2f(input_value)
        print("\n",input_value,"C equal to ",output_value,"F.\n")
    
    print("Do you have another things to convert?")
    print("1. Yes 2. No")
    flag=int(input())
print("Thank you for using my converter :)")
    
    
    
    





