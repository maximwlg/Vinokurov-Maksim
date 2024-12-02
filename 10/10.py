with open('Vinokurov_Maksim_vvod.txt', 'r') as file:
    file_content = file.read()
    print(file_content)
    with open('Vinokurov_Maksim_vivod.txt', 'w') as output_file:
        output_file.write(file_content)