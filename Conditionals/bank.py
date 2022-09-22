def main():
    greeting = input("Greeting: ")
    money(greeting)


def money(x):
    if x.lower().startswith("hello"):
        print("$0")
    elif x.lower().startswith("h"):
        print("$20")
    else:
        print("$100")


main()
