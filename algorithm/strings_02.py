"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""
class Solution:
    def addStrings(self,num1,num2):
        #保存每一位计算的结果
        res_list=[]

        #保存两个字符串的长度
        n1_length = len(num1)
        n2_length = len(num2)

        #将短的那个在左端补0，使得其和长的一样长，方便计算
        if n1_length > n2_length:
            num2 = num2.rjust(n1_length,"0")
        if n2_length  > n1_length:
            num1 = num1.rjust(n2_length,"0")

        #保存补齐后的两个字符串的长度
        n1_pre_length = len(num1)
        n2_pre_length = len(num2)

        #利用列竖式方法遍历求和
        #当前进位为0,即是最开始没有进位
        carry_bit = 0
        for i in range(n1_pre_length):
            #将当前的位置字符转化为整数
            int_n1 = int(num1[n1_pre_length-1-i])
            int_n2 = int(num2[n2_pre_length-1-i])

            #计算求和后的该位置字符
            r = (int_n1 + int_n2 + carry_bit)%10
            #计算当前位置往前一位进位的字符
            carry_bit = int((int_n1+int_n2+carry_bit)/10)
            #将求出的字符数保存在列表中
            res_list.append(str(r))
            #判断最后一位是否有进位，若有则保存进列表
            if carry_bit > 0:
                res_list.append(str(carry_bit))
            #将列表逆置转为字符串返回
            res_list=res_list[::-1]
            res_str = "".join(res_list)
            return res_str

sl = Solution()
r = sl.addStrings("151155999995111","465654564654554564")
print(r)