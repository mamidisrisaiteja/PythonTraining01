#remove duplicates from a list
my_list=[1,1,3,2,1,5,2,7]
my_list = list(set(my_list))
print(my_list)

#find the largest number in a list
my_list2 = [1, 2, 3, 4, 5]
largest_number = max(my_list2)  
print(largest_number)    

#Count occurrences of an element fruits = ['apple', 'banana', 'apple', 'orange']
fruits = ['apple', 'banana', 'apple', 'orange']
apple_count = fruits.count('apple') 
print(apple_count)  # Output: 2