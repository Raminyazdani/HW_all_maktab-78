test = [1, 1, 2, 2, 3, 3, 4, 4, 250, 250, 3, 3, 56, 51, 233, 555, 6, 2, 2222, 1131]
result = list(set(test))
print(result)

# ---------------
result = []
for item in test:
    if item not in result:
        result.append(item)
print(result)
