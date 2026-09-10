with open('data.txt',) as file:
    data = file.read()
    
with open('user_file.txt', 'w') as file:
    file.write("User content")
    
content_capitalized = data.upper()
print(content_capitalized
      ) 
print("Bye! yy")

print("file content: ")
print(content_capitalized)
print("DONE")
