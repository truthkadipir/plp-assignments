def list():
    numbers=input("enter numbers separated by commas: ")
    int_list = [int(i) for i in numbers.split(",")]
    print(sum(int_list))
if __name__ == "__main__":
    list()