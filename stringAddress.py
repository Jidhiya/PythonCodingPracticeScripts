# Immutable Strings Demo

s = "hello"
print("Original string:", s)
print("Memory address:", id(s))

# Modify string (creates new object)
s = s + " world"
print("Modified string:", s)
print("New memory address:", id(s))