import threading

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
rows, cols = len(A), len(B[0])
result = [[0] * cols for _ in range(rows)]

def multiply_cell(i, j):
    result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

threads = [
    threading.Thread(target=multiply_cell, args=(i, j))
    for i in range(rows) for j in range(cols)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

# Display result
for row in result:
    print(row)
