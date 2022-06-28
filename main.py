import hashlib


def lines_count(_file_path):
    file = open(_file_path)
    line_count = 0
    for line in file:
        line_count += 1

    file.close()

    return line_count


def remove_duplicate(_file_path):
    input_file_path = _file_path
    output_file_path = "iplist_sort.txt"

    completed_lines_hash = set()

    output_file = open(output_file_path, "w")

    for line in open(input_file_path, "r"):
        hash_value = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

        if hash_value not in completed_lines_hash:
            output_file.write(line)
            completed_lines_hash.add(hash_value)

    output_file.close()
    return output_file_path


def split_file(_file_path, _ip_numbers):
    file = open(_file_path)
    lines = file.readlines()

    result = ""
    arr = []
    _i = 0
    n = 1

    for line in lines:
        if _i < n * _ip_numbers:
            result += line.replace("\n", ",")
            _i += 1
        else:
            n += 1
            _i += 1
            result = result[:-1]
            arr.append(result)
            result = ''
            result += line.replace("\n", ",")

    if result[-1] == ",":
        result = result[:-1]

    arr.append(result)
    file.close()
    return arr


if __name__ == '__main__':
    ip_block_file_path = input("Enter path to file: ")

    print("Sorting...")
    ip_block_file_path = remove_duplicate(ip_block_file_path)
    line_number = lines_count(ip_block_file_path)

    print("Number of unique IP addresses in file: " + str(line_number))

    ip_object_name = input("Enter ip-object name: ")
    mask = "firewall ip-object add name @" + ip_object_name

    try:
        i = int(ip_object_name[-1])
        mask = mask[:-1]
    except ValueError:
        i = 1

    ip_number = int(input("Enter how many ip should be add in one group: "))

    result_arr = split_file(ip_block_file_path, ip_number)

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
