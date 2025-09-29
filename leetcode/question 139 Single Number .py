# a=[2,2,1]

# for i in range(len(a)):
#     print(a.count(i))
# import copy
# a=[1,[2,3]]
# for i in range(len(a)):
#     print(id(a[i]))

# print(a)
# b=copy.copy(a)
# c=copy.deepcopy(a)
# print(id(a),id(b),id(c))
# print(id(a[1]),id(b[1]),id(c[1]))
# import copy
# data = {"user": {"name": "Devansh", "age": 25}}
# a=copy.deepcopy(data)
# a["user"].update({"name":"Sarthak","age":30})
# print(id(a["user"]["name"]))
# print(id(data["user"]["name"]))
# print(a)
# print(data)
# import copy
# class Author:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Author(name={self.name!r})"

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         return f"Book(title={self.title!r}, author={self.author})"
# author1=Author("Devansh")
# book1=Book("python guide ",author1)
# book2=copy.copy(book1)
# print("before changing")
# print(book1,book2)

# book2.author.name="name chnaged 2"
# book2.title="new python"
# print("\nAfter change:")
# print("book1:", book1)
# print("book2:", book2)

