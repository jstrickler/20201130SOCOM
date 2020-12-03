from glob import glob

py_files = glob('*.py')
print(py_files)
print()

text_files = glob('DATA/*.txt')
print(text_files)
print()

wombat_files = glob('*wombats*')
print(wombat_files)

