# Program for Binary Search

from random import randint          # generate random integer

size = int(input('Enter Size of List : '))
max = int(input('Enter Max digit which you want to insert in the List : '))
srch_elmnt = int(input('Enter Element you want to Search : '))
initial_list = []

# checking whether the inserted number is in the range or not
if srch_elmnt < 0 or srch_elmnt > max:
    print('Searching Element entered should be in between 1 and', max)
    exit()

for lst_ptr in range(size):
    initial_list.append(randint(1, max))

initial_list.sort()

front_ptr = 0
rear_ptr = size-1

print('Randomly Generated List\n', initial_list)

while front_ptr <= rear_ptr:
    mid_ptr = int((front_ptr + rear_ptr)/2)
    if srch_elmnt == initial_list[mid_ptr]:
        print('Element Found at Location {}'.format(mid_ptr+1))
        exit()
    elif srch_elmnt < initial_list[mid_ptr]:
        rear_ptr = mid_ptr-1
    elif srch_elmnt > initial_list[mid_ptr]:
        front_ptr = mid_ptr+1

print('Element Not Found')