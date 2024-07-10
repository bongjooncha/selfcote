# https://code-challenge.elice.io/courses/95930/lectures/738999/lecturepages/20391343
# x = input()
x = "0511"
ans_str = []
ans = 0

if "(" not in x:
    print(len(x))
else:
    for i in range(len(x)-1):
        if x[i].isdigit():
            if x[i+1].isdigit():
                ans_str.append("1+")
            elif x[i+1] == ")":
                ans_str.append("1")
            else: 
                ans_str.append(str(x[i]))
        elif x[i] == "(":
            ans_str.append("*(")
        else:
            if x[i+1] == ")":
                ans_str.append(")")
            else:
                ans_str.append(")*")
    ans_str.append(")")

    print(eval(''.join(ans_str)))