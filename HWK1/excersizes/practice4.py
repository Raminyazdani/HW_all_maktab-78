def reversed1(intest:str):
    
    return intest[::-1]

def reversed2(intest:str):
    intest = list(intest)
    result =[]    
    while intest : result.append(intest.pop())
    return "".join(result)


def reversed3(intest):
    intest = str(intest)
    result = ""
    for item in intest:
        result= item+result
    return result

test = input()
result1=reversed1(test)
result2=reversed2(test)
result3=reversed3(test)

print(result1)
print(result2)
print(result3)
