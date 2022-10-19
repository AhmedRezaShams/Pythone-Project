
MAX, MIN = 1000, -1000



def minimax(depth, nodeIndex, maximizingPlayer,
            v, alpha, beta):
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return v[nodeIndex]

    if maximizingPlayer:

        best = MIN

        # Recur for left and right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, v, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Recur for left and
        # right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, v, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best


# Driver Code
scr = []
x = int(input("enter total num of leaf :"))
for i in range(x):
    y=int(input("enter nodes : "))
    scr.append(y)


depth=int(input("enter depth node : "))
nodeIndex=int(input("enter node values: "))
print("The optimal value is :", minimax(depth, nodeIndex, True, scr, MIN, MAX))

# This code is contributed by Rituraj Jain
