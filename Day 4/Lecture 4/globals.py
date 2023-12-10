" Testing global symbols "


def func():
    " we'll try to access a global variable "
    global my_list
    my_list = [1, 2, 3]
    print(f"func:  {my_list}")


my_list = [7, 8, 9]
print(f"main: {my_list}")
func()
print(f"main: {my_list}")
