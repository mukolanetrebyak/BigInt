def add_BigNumbers(num1, num2):
    if num1 < 0 or num2 < 0:
        raise ValueError("Числа відємні!")
    num1, num2 = str(num1), str(num2)
    len1, len2 = len(num1), len(num2)
    
    if len1 > len2:
        num2 = "0" * (len1 - len2) + num2
    else:
        num1 = "0" * (len2 - len1) + num1

    carry, res = 0, ""
    for i in range(len(num1) - 1, -1, -1):
        s = int(num1[i]) + int(num2[i]) + carry
        carry = s // 10
        res = str(s % 10) + res
    if carry > 0:
        res = str(carry) + res
    
    return int(res)
