def main():
    request = input("what time is it? ")
    time = convert(request)
    if 7 <= time <=8:
        print("breakfest time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("eat nothing")
    

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    final = int(hours) + int(minutes)
    return final

if __name__ == "__main__":
    main()
