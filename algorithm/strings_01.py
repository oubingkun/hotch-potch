"""
每日leetcode--415
给定两个字符串形式非负整数num1,num2,计算和
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""
"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""
"""
手算加法步骤，考虑进位即可
"""
class AddString(object):
    def addString(self,num1,num2):
        result = '' #保存两个字符串长度
        i,j = 0
        carry = 0 #是否进位
        while i < len(num1) or j < len(num2):
            x,y=0,0
            if i < len(num1):
                x = int(num1[len(num1)-1-i])
            if j < len(num2):
                y = int(num2[len(num2)-1-i])
            this_num = (x+y+carry)%10
            carry = (x+y+carry)/10 #更新进位
            result = str(this_num)+result
            i+=1
            j+=1
        if carry ==1: #位数边长
            result = '1' + result
        return result


