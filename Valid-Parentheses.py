def isValid(s: str):
    st = []
    mp = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i in s:
        if i == '(' or i == '{' or i == '[':
            st.append(i)
        elif i == ')' or i == '}' or i == ']':
            if not len(st) or mp[i] != st[-1]:
                return False
            else:
                st.pop()

    return  len(st)==0