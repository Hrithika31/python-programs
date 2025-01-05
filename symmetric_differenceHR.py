m = int(input())
a = set(map(int, input().strip().split()))

n = int(input())
b = set(map(int, input().strip().split()))

symmetric_diff = a.symmetric_difference(b)

for elem in sorted(symmetric_diff):
    print(elem) 