name='Danil'
print(name)

age='18'
print('my name is',name,'im ', age, 'years old.')

print((name+' ')*5)

yourname=str(input('whats your name?'))
while (yourname.isspace()) or (' ' in yourname):
    print ('write your name without "Space"')
    yourname = str(input('whats your name?'))
yourage=int(input('how old are u, bro?'))
while (yourage<0) or (yourage>150):
    print('write right age')
    yourage = int(input('how old are u, bro?'))
print('wassup,', yourname)
print('ouh, do you know what goes up and never goes dowm? your age')

yourage = int(yourage)
if yourage<18:
    print('we are sorry but you dont have access to pronhub :(')
if yourage>=18:
    print('welcome to github')

print(yourname[1:-1])
print(yourname[::-1])
print(yourname[0:5])

print('in the name of the letters:', len(yourname))
sum=0
umbo=1
while yourage>0:
    chislo=yourage%10
    sum=sum+chislo
    umbo=umbo*chislo
    yourage=yourage//10
print('the sum of the age numbers:', sum)
print('the product of age numbers:', umbo)

print(yourname.upper())
print(yourname.lower())
print(yourname.title())
print(yourname.swapcase())

print('can you solve the example? 6-1*0+6/6')
answer = input()
while answer != 'yes':
    print('you didnt guess')
    answer = input()
print ('you guessed it')
