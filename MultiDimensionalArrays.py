worlds_list = [[1,2,3], 
               [1,2,3,4], 
               [1,2], 
               [1,2,3,4,5,6]]
# I didn't think you could do this in Python
# 2D Arrays don't all need to be the same size
# This example is a list of "worlds" in a video game with the "levels" for each of those worlds

ninth_world = worlds_list[2][1]
# Obviously you want to grab the "row" (the element in the larger list)
# Then grab the "column" (the element in the smaller list)
print(ninth_world)
# expected : 2

worlds_list.append([1,2,3,4,5])
print(worlds_list)
# expected : [[1,2,3], [1,2,3,4], [1,2], [1,2,3,4,5,6], [1,2,3,4,5]]

worlds_list[1].pop()
print(worlds_list)
# expected : [[1,2,3], [1,2,3], [1,2], [1,2,3,4,5,6], [1,2,3,4,5]]


# Nothing really new hear, we're still doing list operations we're just going one more "layer" deep
# All methods that would apply to lists apply here to the elements within the lists because 
#       the elements are themselves, lists.