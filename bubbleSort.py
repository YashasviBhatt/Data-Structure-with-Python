# Creating function for swapping of values
def Swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

# Creating function for Bubble Sort Algorithm
def BubbleSort(input_list):
    for lst_ptr1 in range(len(input_list)):
        for lst_ptr2 in range(len(input_list)-lst_ptr1-1):
            if input_list[lst_ptr2] > input_list[lst_ptr2+1]:
                input_list[lst_ptr2], input_list[lst_ptr2+1] = Swap(input_list[lst_ptr2], input_list[lst_ptr2+1])
    return input_list

# taking Unsorted List as input from user
initial_list = list(map(int, input('Enter List\n').split()))

# Checking whether an empty input list is inserted or not
if len(initial_list) == 0:
    print('Empty List can\'t be sorted')
    exit()

# If list contains single items then there is no need of applying Sorting Algorithm
elif len(initial_list) == 1:
    print('Sorted List\n',initial_list)
    exit()

# Calling BubbleSort() function with initial_list passed as parameter
else:
    sorted_list = BubbleSort(initial_list)
    print('Sorted List\n', sorted_list)