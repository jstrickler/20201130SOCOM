from president import President


p = President(26)

print(p)
print(p.first_name, p.last_name, '\n')

atts = ['first_name', 'last_name']

for att in atts:
    print(getattr(p, att))

if hasattr(p, "to_json"):
    to_json = getattr(p, "to_json")
    to_json()
else:
    print("DOES NOT HAVE")

def get_initials(self):
    return self.first_name[0] + self.last_name[0]

setattr(President, 'get_initials', get_initials)

print(p.get_initials())

#  getattr() hasattr() setattr() delattr()







