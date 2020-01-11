def parse(args):
    filename = args.input_path

    with open(filename) as file_in:
        content = file_in.readlines()
    content = [x.strip() for x in content]
    
    blank_index = 0
    for counter, value in enumerate(content):
        if value == "":
            blank_index = counter
    original = content[1:blank_index]
    desired = content[blank_index+2:]

    return original, desired
