import hashlib


def lines_count(input_file_path):
    with open(f"{input_file_path}", 'r') as file:
        line_count = len(file.readlines())

    return line_count


def remove_duplicate(input_file_path):
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


def split_file(input_file_path, _ip_numbers):
    file = open(input_file_path)
    lines = file.readlines()

    result = ""
    arr = []
    _i = 0
    n = 1

    for line in lines:
        if _i < n * _ip_numbers:
            line = line.strip() + ","
            result += line
            _i += 1
        else:
            n += 1
            _i += 1
            result = result[:-1]
            arr.append(result)
            result = ''
            line = line.strip() + ","
            result += line

    if result[-1] == ",":
        result = result[:-1]

    arr.append(result)
    file.close()
    return arr


def define_number(_ip_object_name):
    _user_number = ""

    for i in range(-1, -len(_ip_object_name), -1):
        try:
            last_digit = int(_ip_object_name[i])
            _user_number += str(last_digit)
        except ValueError:
            if i == -1:
                _user_number += "1"
            break

    return int(_user_number[::-1])


def write_file(_result_arr, _user_number, _mask):
    with open("result.txt", "w") as result_file:
        for ips in _result_arr:
            firewall_rule = f"{_mask}{_user_number} {ips}\n"
            result_file.write(firewall_rule)
            _user_number += 1


if __name__ == '__main__':
    ip_block_file_path = input("Enter path to file: ")

    print("Remove duplicate...")
    ip_block_file_path = remove_duplicate(ip_block_file_path)
    lines_number = lines_count(ip_block_file_path)

    print(f"Number of unique IP addresses in file: {lines_number}")

    ip_object_name = input("Enter ip-object name: ")
    mask = f"firewall ip-object add name @{ip_object_name}"

    ip_number = int(input("Enter how many ip should be add in one group: "))

    result_arr = split_file(ip_block_file_path, ip_number)

    user_number = define_number(ip_object_name)
    user_number_length = len(str(user_number))
    if user_number_length > 1:
        mask = mask[:-len(str(user_number))]

    write_file(result_arr, user_number, mask)

    #
    # if you need print into console
    #
    # for ips in result_arr:
    #     print(mask + str(i) + ' ' + ips)
    #     i += 1
    #
