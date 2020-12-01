def main():
    f = readFile('numbers.txt')
    array_length = len(f)
    for x in range(array_length):
        for y in range(array_length):
            for j in range(array_length):
                result = checkSum(f[x], f[y], f[j])
                if result == int(2020):
                    print(result)
                    finalResult = int(f[x]) * int(f[y]) * int(f[j])
                    return finalResult

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

def checkSum(num1, num2, num3):
    result = int(num1) + int(num2) + int(num3)
    return result

print(main())
