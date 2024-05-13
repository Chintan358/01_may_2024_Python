
def test():
    try:
        a  =int(input("enter a : "))
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
     print("hello...function completed..")

k = test();
print(k)