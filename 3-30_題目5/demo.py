"""
83, 41, 72, 58, 61, 36

氣泡排序法
將序列從小排到大，序列中的數字兩兩比較，把小的數字往前面移動
"""

def bubble(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                j+1 # python 的 range 會自己+1，不用這樣搞剛
            elif list[i] > list[j]:
                num = list[i]
                list[i] = list[j]
                list[j] = num
            # print(str(i) + 'round : ' + str(list))
    return list

if __name__ == '__main__':
    list = [83, 41, 72, 58, 61, 36]
    print('origin : ' + str(list))
    ans = bubble(list)
    print('小到大排序為 : ' + str(ans))
