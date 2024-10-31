
def remove(string):
    count_before = len(string)
    string = string.replace('.', '')
    count_after = len(string)
    removed_count = count_before - count_after
    return string, removed_count
input_string = input()
new_string, count = remove(input_string)
print (f'Новая строка: {new_string}')
print (f'Количество удаленных символов:{count}')