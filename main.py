user_input = input("Enter some text: ")

with open('data.txt',) as file:
    data = file.read()
    
with open('user_file.txt', 'w') as file:
    file.write(user_input)
    
content_capitalized = data.upper()
print("Bye! yy")

print("file content: ")
print(content_capitalized)
print("DONE")
  