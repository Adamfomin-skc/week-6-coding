ans = input('Do you want to input a result ?: ')
if ans == 'yes':
    name = input('Enter a students name: ')
    subject = input('Enter a subject: ')
    mark= int(input('Enter a result: '))
    if mark > 100:
        print('Not a valid mark')
        
    if mark >= 90:
        result= ('H1')
    elif mark >=80:
        result= ('H2')
    elif mark >= 70:
        result= ('H3')
    elif mark >=60:
        result= ('H4')
    elif mark >= 50:
        result= ('H5')
    elif mark>= 40:
        result= ('H6')
    elif mark >=30:
        result= ('H7')
    else:
        result = ('FAIL')
   

#print('Name:', name,'subject:',subject, 'Result:',result )

else:
    print('Ok maybe another time')

print('Name:', name,'------','subject:',subject,'------', 'Result:',result )
