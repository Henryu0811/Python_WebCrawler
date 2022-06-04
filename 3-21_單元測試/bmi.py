def calculate(w, h):
    return round(w/h**2, 2)

def cmToM(cm):
    return cm/100

if __name__ == '__main__': # 為True的話，代表是 bmi.py 單獨執行
    import unittest

    class BmiTestCase(unittest.TestCase): # 繼承類別 TestCase

        def test_calculate(self): # 類別中的函式命名開頭都要是 test
            result = calculate(65, 1.75) # 實作測試的結果，呼叫上方函式，並傳給變數 result
            # 判斷程式結果是否正確，用類別 TestCast 中的函式 assertEqual，前面放我們期望的結果，後面放函式計算後的結果
            self.assertEqual(21.22, result)
            # 以上完成函式 calculate 的 "測試案例 (test case)"

        def test_cmToM(self):
            result = cmToM(175)
            self.assertEqual(1.75, result)
            # 以上完成函式 cmToM 的 "測試案例 (test case)"

        # 建立好 test case 後，把要測試的案例放到一個 list 中
    tests = [
        BmiTestCase('test_calculate'), # 類別 BmiTestCase 中，放入要測試的函式名稱
        BmiTestCase('test_cmToM')
    ]
    # 建立一個物件 TestSuite 命名為 suite
    suite = unittest.TestSuite()
    suite.addTests(tests) # 用測試套件中的函式 addTests，將 tests 放入套件中

    # 最後用測試執行器運作
    # 建立一個物件 TextTestRunner 命名為 runner
    runner = unittest.TextTestRunner()
    runner.run(suite) # 使用物件中的函式 run() 進行測試，將套件 suite 放到參數中

    # 執行後可以知道，run 了幾次，花了多少時間
    # OK 則是代表測試正確

    #以上測試，是在系統上線前可以測試，確保更動後的函式能夠正常運作