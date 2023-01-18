def div(a,b):
    try:
        c = ((a+b)/(a-b))

    except ZeroDivisionError:
        print("ZeroDivisionError")

    else:
        print(c)

    finally:
        print("Run anyway")


div(5,5)