# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# T.C O(digits+operator = n) S.C o(digits)
# corner case -6/132 or -1/22
class Solution:
    def evalRPN(self, tokens):
        from collections import deque as stack
        st = stack()
        for ch in tokens:
            if ch == '+':
                st.append(st.pop()+st.pop())
            elif ch == '*':
                st.append(st.pop()*st.pop())
            elif ch == '-':
                y = st.pop()
                x = st.pop()
                st.append(x-y)
            elif ch == '/':
                flag = 1
                y = st.pop()
                x = st.pop()
                st.append(int(float(x)/float(y)))
            else:
                st.append(int(ch))
        return st.pop()
obj=Solution()
print(obj.evalRPN(["2","1","+","3","*"]))