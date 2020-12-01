from struct import Struct

bmp_header = Struct("=hihhi")

print("length of header:", bmp_header.size)

with open('DATA/map.bmp', mode='rb') as map_in:
    raw_data = map_in.read(bmp_header.size)
    print(len(raw_data))
    file_type, bmp_size, _, _, data_offset = bmp_header.unpack(raw_data)
    print(f"header: {file_type:02x} size: {bmp_size}  offset: {data_offset}")


print("In Durham it is 66\u00B0")

s = "In Durham it is 66\u00B0"
print(s)
print(len(s))
b = s.encode()
print(b)
print(len(b))
print(type(s), type(b))

s2 = b.decode(errors='ignore')
print(s2, len(s2), type(s2))

# UNICODE input
# STRING processing
# UNICODE output

# bytes str
print(s[0], b[0])
