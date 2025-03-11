def list1():
    my_list = []
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    my_list.insert(1, 15)
    my_list.extend([50, 60, 70])
    del my_list[-1]
    my_list.sort()
    print(my_list.index(30))
if __name__ == "__main__":
    list1()