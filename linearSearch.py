import random as rn

initial_list = []

list_size = int(input('Enter List Size : '))
srch_elmnt = int(input('Enter Element you want to search : '))

if srch_elmnt > 30 or srch_elmnt < 1:
    print('Enter Search Element between 1 and 30')
    exit()

# Creating random list using the randint function of random module
for lst_ptr in range(list_size):
    initial_list.append(rn.randint(1, 5))

flag=0

for lst_ptr in range(list_size):
    if srch_elmnt == initial_list[lst_ptr]:
        print('Element Found at location number {}'.format(lst_ptr+1))
        flag = 1

if flag == 0:
    print('Element Not Found')

print('The Randomly Created List\n',initial_list)