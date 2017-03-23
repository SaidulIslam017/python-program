print('**Teacher Log in page**')
username = ['Noyon','saidul islam','sumon']
password = ['01741','01742','01743']
userName = input('please Enter user name:')
Password = input('please Enter password:')
if(userName in username and Password in password):
 if username.index(userName) == password.index(Password):
     print('***Log in succes*** ')
     print('***Welcome Student profile for Teacher***')

     Name = 'saidul islam'
     mobile = '01742080220'

     print('Name:', Name)
     print('Mobile:',mobile)
     Number = input('Please Enter Number: ')
     if Number > '79':
         print('Grade: A+')
     elif Number > '74' and Number < '80':
         print('Grade: A')
     elif Number > '69' and Number < '75':
         print('Grade: A-')
     elif Number > '64' and Number < '70':
         print('Grade: B+')
     elif Number > '59' and Number < '65':
         print('Grade: B')
     elif Number > '54' and Number < '60':
         print('Grade: C')
     else:
         print('Fail')
 else:
     print(':Log in Failed:')