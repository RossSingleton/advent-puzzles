def main():
    f = readFile('numbers.txt')
    array_length = len(f)
    for x in range(array_length):
        for y in range(array_length):
            result = checkSum(f[x], f[y])
            if result == int(2020):
                print(result)
                finalResult = int(f[x]) * int(f[y])
                return finalResult

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

def checkSum(num1, num2):
    result = int(num1) + int(num2)
    return result

print(main())
