import sys
A = [3423, 243, 12, 4141, 166756, 845]

for i in range(len(A)):

    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print("Sorted Array")
for i in range(len(A)):
    print("%d" %A[i], end=" ")

print()