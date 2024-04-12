def averageComparisons(numbers):
    comparisons = 0
    for x in numbers:
        comparisons += binarySearch(x, numbers)
    return comparisons / len(numbers)


def binarySearch(target, numlist):
    low = 0
    high = len(numlist) - 1
    counter = 0
    while True:
        mid = int((low + high) / 2)
        if numlist[mid] == target:
            counter += 1
            break
        else:
            if numlist[mid] < target:
                low = mid + 1
                counter += 1
            else:
                high = mid - 1
                counter += 1
    return counter


if __name__ == '__main__':
    num = []
    i = int(input("Input any number: "))
    # Note: input 0 to break out of this loop
    while i:
        num.append(i)
        i = int(input("Input more numbers (0 breaks loop): "))

    print("On average, " + str(averageComparisons(num)) + " comparisons will be required.")
