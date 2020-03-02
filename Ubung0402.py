dw = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
k = [dw[i] for i in range(len(dw)) if i-1 > 0 if dw[i - 1] < dw[i]]
print(k)
