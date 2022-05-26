

def seacher_data(task):
    with open('phonebook.txt', 'r') as file:
        my_file = file.read()
        my_file1 = my_file.split('\n')
        flag = False
        user_error = 'No this contact, try again '
        for i in my_file1:
            if task in i:
                flag = True
                result = i
        if flag:
            return result
        else:
            return user_error
