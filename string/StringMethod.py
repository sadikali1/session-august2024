a = "python"

print(a.capitalize())

b = "this is python programming python python"
print(b.count("python"))
print(b.count("python", 1, 20))

print(b.startswith("this"))
print(b.endswith("python"))

b = "343543G"
print(b.isdigit())
print(b.isalnum())

print(len(b))

b = "            Python           "
print(b.rstrip())
print(b.lstrip())
print(b.strip())

b = "python proGraM"
print(b.title())

print(b.upper())
print(b.lower())
