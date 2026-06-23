def isMultiple3(x):
    return x%3==0
def isMultiple5(x):
    return x%5==0
sum=0
mainlist = [i for i in range(0,1000)]
for each in mainlist:
    if isMultiple3(each) or isMultiple5(each):
        sum += each
print(sum)