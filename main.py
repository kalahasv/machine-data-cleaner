from data_clean import clean_data

def get_input():
    file_path = input('File path:')
    type = input('Type:')
    #put error checking here
    return file_path,type


if __name__ == '__main__':
    print("Program running...")
    inputs = get_input()
    clean_data(inputs)

    