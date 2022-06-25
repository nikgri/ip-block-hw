def lines_count(_file_path):
    file = open(_file_path)
    line_count = 0
    for line in file:
        line_count += 1

    file.close()

    return line_count


def split_file(_file_path):
    file = open(_file_path)
    lines = file.readlines()

    result = ''
    arr = []
    _i = 0
    n = 1

    for line in lines:
        if _i < n * 1000:
            result += line.replace('\n', ',')
            _i += 1
        else:
            n += 1
            _i += 1
            result = result[:-1]
            arr.append(result)
            result = ''
            result += line.replace('\n', ',')

    file.close()
    return arr


if __name__ == "__main__":
    ip_block_file_path = input("Enter path to file with: ")
    line_number = lines_count(ip_block_file_path)

    print("Number of IP addresses: " + str(line_number))

    ip_object_name = input('Enter ip-object name: ')
    mask = 'firewall ip-object add name @' + ip_object_name

    result_arr = split_file(ip_block_file_path)
    i = 0

    #
    # if you need print into console
    #
    # for ips in result_arr:
    #     print(mask + str(i) + ' ' + ips)
    #     i += 1
    #

    with open("result.txt", "w") as result_file:
        for ips in result_arr:
            result_file.write(mask + str(i) + ' ' + ips + '\n')
            i += 1
