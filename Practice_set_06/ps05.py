#### Write a program to find out whether a given post is talking about Pranta or not.

post = input("Write your post: ")

if "Pranta".lower() in post.lower():
    print("This post is talking about pranta.")
else:
    print("This post is not talking about pranta.")