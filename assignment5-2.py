import random

a = input('����/����/�� : ')

if a== '����':
    a = 1
elif a =='����' :
    a=2
elif a== '��':
    a =3

b = random.randint(1,3)

if b == 1:
    b='����'
if b==2:
    b='����'
if b==3:
    b='��'

print('��ǻ�� :',b)

if b =='����':
    b=1
if b =='����':
    b=2
if b=='��':
    b=3

if a+1==b or a-2==b:
    print('�й�')
elif a-1==b or a+2 == b:
    print('�¸�')
else:
    print('���º�')
