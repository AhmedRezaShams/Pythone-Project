
#maximum,minimum = int(input("enter value of alpha -infinity")),int(input("enter value of beta infinity"))
maximum , minimum = 1000, -1000


def fun_alphabeta(d, node, maxP, v, A, B):

    if d==3:
        return v[node]
    if maxP:
        best = minimum
        for i in range(0,2):
            value = fun_alphabeta(d + 1, node * 2 + i, False, v, A, B)
            best = max(best, value)
            A = (A, best)
            if B<=A:
                continue
            break
        return best
    else:
        best = maximum
        for i in range(0,2):
            value = fun_alphabeta(d + 1,node * 2 + i, True, v, A, B)
            best = min(best,value)
            B = min(B,best)
            if B<=A:
                break
        return best

scr = []
x = int(input("enter total num of leaf :"))
for i in range(x):
    y=int(input("enter nodes : "))
    scr.append(y)


d=int(input("enter depth node : "))
node=int(input("enter node values: "))
print("the optimal sol : ", fun_alphabeta(d, node, True, scr, minimum, maximum))

