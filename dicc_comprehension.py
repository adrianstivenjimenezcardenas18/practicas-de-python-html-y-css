def run():
    my_dict = {i:i**2 for i in range(1,1001) if i % 2 == 0}
    print(my_dict)
if __name__ == '__main__':
    run()