with open("practice.txt", "r") as f:
    data = f.read()

    num = ""
    for c in data:
        if(c == ","):
            print(int(num))
            num == ""
        else:
            num += c
        