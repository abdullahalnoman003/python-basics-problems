import math

scores = [1, 0, 0, 3] # This is my ids last 4 digit (232-35-003)
height = 2
minimax_leaf_nodes = 0
alphabeta_leaf_nodes = 0

# ------------------ Minimax ------------------
def minimax(depth, nodeIndex, isMax, scores, height):
    global minimax_leaf_nodes
    if depth == height:
        minimax_leaf_nodes += 1
        return scores[nodeIndex]
    if isMax:
        left = minimax(depth + 1, nodeIndex * 2, False, scores, height)
        right = minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        return max(left, right)
    else:
        left = minimax(depth + 1, nodeIndex * 2, True, scores, height)
        right = minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        return min(left, right)

# ---------------- Alpha-Beta Pruning ----------------
def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, height):
    global alphabeta_leaf_nodes
    if depth == height:
        alphabeta_leaf_nodes += 1
        return scores[nodeIndex]
    if isMax:
        best = -math.inf
        # Left Child
        best = max(
            best,
            alphabeta(depth + 1, nodeIndex * 2, False, scores, alpha, beta, height),
        )
        alpha = max(alpha, best)
        # Right Child (only if not pruned)
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
        # Left Child
        best = min(
            best, alphabeta(depth + 1, nodeIndex * 2, True, scores, alpha, beta, height)
        )
        beta = min(beta, best)
        # Right Child (only if not pruned)
        if alpha < beta:
            best = min(
                best,
                alphabeta(
                    depth + 1, nodeIndex * 2 + 1, True, scores, alpha, beta, height
                ),
            )
        return best

# ---------------- Main ----------------
minimax_result = minimax(0, 0, True, scores, height)

alphabeta_result = alphabeta( 0, 0, True, scores, -math.inf, math.inf, height)

print("Minimax Result:", minimax_result)
print("Alpha-Beta Result:", alphabeta_result)
print("Leaf Nodes Evaluated (Minimax):", minimax_leaf_nodes)
print("Leaf Nodes Evaluated (Alpha-Beta):", alphabeta_leaf_nodes)
