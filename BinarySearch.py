#二分探索 (Binary Search)

data = [1, 3, 7, 13, 17, 21, 74,96]

def binary_search(data, key):
    start = 0
    end = len(data) - 1

    while (start <= end):
        # //で商を求める
        middle = (start + end) // 2
        print(middle)
        if data[middle] == key:
            return middle
        elif data[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
    return "false"

print(binary_search(data, 13))
#test用
#test用　main