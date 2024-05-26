# https://leetcode.com/problems/masking-personal-information/
# runtime: 86.67%
# memory: 100%
def maskPII(s):
    """
    :type s: str
    :rtype: str
    """
    if (ord(s[0]) >= 97 and ord(s[0]) <= 122 or ord(s[0]) >= 65 and ord(s[0]) <= 90):
        s = list(s)
        check = None
        if (s[0].isupper()):
            s[0] = s[0].lower()
        for i in range(len(s) - 1):
            if (ord(s[i + 1]) == ord('@')):
                if (s[i].isupper()):
                    s[i] = s[i].lower()
                check = i
            if check != None:
                if (s[i+1].isupper()):
                    s[i+1] = s[i+1].lower()

        s = list(s[0]) + list(s[check:])
        s.insert(1, '*****')
        return "".join(s)
    else:
        s = list(s)
        control = 0
        for let in s:
            if let.isnumeric():
                control += 1
        control -= 10
        out = ""
        out += '+' if control != 0 else ''
        out += '*' * control
        out += '-' if control > 0 else ''
        out += "***-***-"
        control = []
        for i in range(len(s) - 1, 0, -1):
            if s[i].isnumeric():
                control.insert(0, s[i])
                if len(control) == 4:
                    break
        return out + "".join(control)

# s = "LeetCode@LeetCode.com"
# s = "1(234)567-890"
# s = "AB@qq.com"
# s = "1(234)567-890"
s = "86-(10)12345678"

print(maskPII(s))

