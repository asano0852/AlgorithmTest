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
#test用　test-1-1-1 追記1 追記2
#test用　test-1 commit　追加1
#test用　test-1 追記1 追記2
#test用 test-1 追記1 追記2 追記3
#test用2
#test用2-1 commit追加
#test用2-1 checkout後HEADからブランチ作成 さらにcommit追加
#test用　test-1-1-1 追記1 追記2

#test3 追記1
