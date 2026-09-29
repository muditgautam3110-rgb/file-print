try:
    with open('data.txt',) as file:
        data = file.read()
    
    content_capitalized = data.upper()
    print(content_capitalized)
    print("Hello! xx")
    print("Bye! yy")  
    print("file content: ")
    
    user_input = input("Enter some text: ")
    
    with open('user_file.txt', 'w') as file:
        file.write(user_input)
    
    content_capitalized = data.upper()
    print("Bye! yy")

    print("file content: ")
    print(content_capitalized)
    print("DONE")
  
        
except FileNotFoundError:
    print("File not found.")
     

