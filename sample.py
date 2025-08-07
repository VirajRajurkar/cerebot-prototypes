while True:
    viraj = input("Hello")

    if viraj.lower() == "exit":
        print("Goodbye")
        break

    elif viraj.lower() == "hello": 
        print("Hi there! How can I assist you today?")

    else:
        print("You said:", viraj)

