example = 'Топинамбур'

def midIndex(inputString):
    if(isinstance(inputString,str)):
        if(len(inputString)%2>=5):
            return int(len(inputString)/2)+1
        else:
            return int(len(inputString)/2)
    else:
        return -1 #error code



middleIndex = midIndex(example)
print(example[0])
print(example[-1])
if(middleIndex != -1):
    print(example[middleIndex:])
print(example[::-1])
print(example[1::2])

