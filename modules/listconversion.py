
def list_conversion():
    l = list(input("Enter list: "))
    s= set(l)
    return s

if __name__ == "__main__":
    result = list_conversion()
    print(result)