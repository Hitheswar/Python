class file_handle:
    filename = "H:\SA\Support Activities.txt"
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line)
