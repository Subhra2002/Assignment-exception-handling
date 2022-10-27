def compute():
    try:
        a = 5/0
        print(a)
    except ZeroDivisionError as e:
        print("Make sure you are not dividing by 0")
compute()