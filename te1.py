def cyz(digits):
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res = []
    # print(len(digits))
    if len(digits) == 0:
        return []
    # 单个数字
    if len(digits) == 1:
        # d=digits[0]
        return keyboard[digits[0]]
    # 两个数字
    for i in keyboard[digits[0]]:
        for j in keyboard[digits[1]]:
            res.append((j + i))
    return res
print(cyz(['9', '9']))
print(cyz("99"))
