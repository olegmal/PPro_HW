

def new_format(string):
    reversed_string = string[::-1]
    formatted_string = ".".join(reversed_string[num:num + 3] for num in range(0, len(reversed_string), 3))

    return formatted_string[::-1]


assert (new_format("0") == "0")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("10000") == "10.000")
assert (new_format("100000") == "100.000")
assert (new_format("1000000") == "1.000.000")
