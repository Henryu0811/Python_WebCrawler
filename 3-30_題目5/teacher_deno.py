"""
83, 41, 72, 58, 61, 36

氣泡排序法
將序列從小排到大，序列中的數字兩兩比較，把小的數字往前面移動
"""

def bubble(list):
    for round in range(1, len(list)):
        for i in range(0, len(list)-round):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        print(str(round) + ' round :' + str(list))
    return

if __name__ == '__main__':
    list = [83, 41, 72, 58, 61, 36]
    print('origin : ' + str(list))
    bubble(list)