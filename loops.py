single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
cubes = [cube**3 for cube in single_digits if cube < 10]
for single in single_digits:
  if single < 10:
    print(single)
    squares.append(single**2)
print(squares)
print(cubes)