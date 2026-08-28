import math


def minimax(currentDepth, nodeIndex, isMax, scores, height, path):

    if currentDepth == height:
        return scores[nodeIndex], path
    if isMax:
        leftScore, leftPath = minimax(
            currentDepth + 1, nodeIndex * 2, False, scores, height, path + " -> Left"
        )
        rightScore, rightPath = minimax(
            currentDepth + 1, nodeIndex * 2 + 1, False, scores, height, path + " -> Right",
        )
        if leftScore >= rightScore:
            return leftScore, leftPath
        else:
            return rightScore, rightPath
    else:
        leftScore, leftPath = minimax(
            currentDepth + 1, nodeIndex * 2, True, scores, height, path + " -> Left"
        )
        rightScore, rightPath = minimax(
            currentDepth + 1,nodeIndex * 2 + 1, True, scores, height, path + " -> Right",
        )
        if leftScore <= rightScore:
            return leftScore, leftPath
        else:
            return rightScore, rightPath

scores = []

terminal = int(input("Enter the number of Terminal Nodes (Power of 2): "))

if terminal <= 0 or (terminal & (terminal - 1)) != 0:
    print("Error: Number of terminal nodes must be a power of 2 (2, 4, 8, 16, ...)")
    exit()

for i in range(terminal):
    score = int(input(f"Enter score {i + 1}: "))
    scores.append(score)

height = int(math.log(terminal, 2))

optimalScore, optimalPath = minimax(0, 0, True, scores, height, "Root")

print(f"Optimal Score : {optimalScore}")
print(f"Optimal Path  : {optimalPath}")
