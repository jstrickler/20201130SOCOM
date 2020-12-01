
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)

print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_text = mary_in.read()
    print("raw")
    print(repr(all_text))
    print("cooked")
    print(all_text)

print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)

print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    all_lines_without_nl = contents.splitlines()
    print(all_lines_without_nl)

print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)


# open('FILENAME', 'mode')

#  'r' 'w' 'a' 'x'
#  'rb' 'wb' 'ab' 'xb'


with open('junk.txt', 'w') as junk_out:
    junk_out.write("whatever\n")


with open('DATA/mary.txt', 'rb') as mary_in:
    contents = mary_in.read()
    print(contents)






