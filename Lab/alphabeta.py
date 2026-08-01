import math

leaf_nodes = 0


def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, height):

    global leaf_nodes

    if depth == height:
        leaf_nodes += 1
        return scores[nodeIndex]

    if isMax:

        best = -math.inf

        best = max(
            best,
            alphabeta(depth + 1, nodeIndex * 2, False, scores, alpha, beta, height),
        )
        alpha = max(alpha, best)
        if alpha < beta:
            best = max(
                best,
                alphabeta(
                    depth + 1, nodeIndex * 2 + 1, False, scores, alpha, beta, height
                ),
            )
        return best
    else:
        best = math.inf
        best = min(
            best, alphabeta(depth + 1, nodeIndex * 2, True, scores, alpha, beta, height)
        )
        beta = min(beta, best)
        if alpha < beta:
            best = min(
                best,
                alphabeta(
                    depth + 1, nodeIndex * 2 + 1, True, scores, alpha, beta, height
                ),
            )
        return best


scores = [5, 6, 2, 8]

height = 2

result = alphabeta(0, 0, True, scores, -math.inf, math.inf, height)

print(result)
print("Leaf Nodes =", leaf_nodes)
