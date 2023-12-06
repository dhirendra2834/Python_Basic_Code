
# tuples 
a=(1,2,3,'d',"Dhirendra")

print(a)

# difference between list vs tuples 
'''
Mutability:
List: Lists are mutable, which means you can modify their elements after the list is created. You can add, remove, or change items in a list.
Tuple: Tuples are immutable. Once a tuple is created, you cannot modify its elements. You can't add, remove, or change items in a tuple.

Syntax:
List: Lists are defined using square brackets [].
Tuple: Tuples are defined using parentheses ().


Performance:
List: Due to their mutability, lists might require more memory and can be slightly slower than tuples in certain operations.
Tuple: Tuples are generally more memory-efficient and might have slightly faster access times.


Use Cases:
List: Use lists when you need a collection that can be modified, such as when you want to add or remove elements dynamically during the program's execution.
Tuple: Use tuples when you want an immutable collection, especially for cases where the data should remain constant throughout the program. Tuples are also used in scenarios where the order and structure of the data are important, like representing coordinates (x, y) or RGB color values (red, green, blue).

Methods:
Both lists and tuples have some common methods, but since lists are mutable, they have more methods related to modification, while tuples have fewer methods related to that.
'''