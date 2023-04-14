list = [1, 2, 3, 4, 5]
new_list = [2 * num for num in (1,2,3,4,5)]
new_list_1 = [2 * num for num in list]
new_list_2 = [2 * num for num in list if num < 5]
new_list_3 = [2 * num for num in list if num < 5 and num > 2]

print(list)
print(new_list)
print(new_list_1)
print(new_list_2)
print(new_list_3)

list_pairs_1 = [(a, b) for a in (1, 3, 5) for b in (2, 4, 6) if a > b]
list_pairs_2 = [(a, b, c) for a in (1, 3, 5) for b in (2, 4, 6) for c in (7, 8, 9)]
print(list_pairs_1)
print(list_pairs_2)

print([x.capitalize() for x in ['cat', 'dog', 'cow']])
print([x.upper() for x in ['cat', 'dog', 'cow']])
print(["".join(x[::-1]) for x in ['cat', 'dog', 'cow']])
print(["".join(x[::-1]) for x in ['cat', 'dog', 'cow'] if "o" in x])

#Create the reversed pairs in tuples
reverse = lambda x: "".join(x[::-1])
animals = ["cat", "dog", "cow", "maki", "majom"]
print([(a, b) 
       for a in animals 
       for b in ["".join(x[::-1]) for x in animals] #reverse the animals item
       if (lambda x: "".join(x[::-1]))(a) == b]) #filter if the a reversed == b reversed, but keep a unchanged

#The more readable version and in list
print([[a, b] 
       for a in animals 
       for b in [reverse(x) for x in animals] #reverse the animals item
       if reverse(a) == b]) #filter if the "a" reversed == "b" reversed, but keep "a" unchanged
