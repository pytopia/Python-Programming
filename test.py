def greet(name):
    greeting = f"Hello, {name}!"
    return greeting

def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()