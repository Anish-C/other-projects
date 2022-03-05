
x=True
List=[]
while (x):
    number=input('number:')
    print (bool(number))
    print(number.isdigit())

    if bool(number)==True:
        if number.isdigit()==True:
            List.append(number)
            print(List)
            print(min(List))
            print(max(List))
            question=input('do you want to do it again')
            if question=='yes':
                x=True
            else:
                print('quit')
                x=False
        else:
                print('please put in a digit')
    else:
        print('please put in a digit')
    
