try:
    with open('data.txt',) as file:
        data = file.read()
    
    content_capitalized = data.upper()
    print(content_capitalized)
    print("Hello! xx")
    print("Bye! yy")  
    
    user_input = input("Enter some text: ")
    
    with open('user_file.txt', 'w') as file:
        file.write(user_input)
    
    content_capitalized = data.upper()
    print("Bye! yy")

    print("file content: ")
    print(content_capitalized)
    print("DONE")

    n = 10
    for i in range(n):
        if i % 2 == 0:
            print(i)
  
        
except FileNotFoundError:
    print("File not found.")
     
