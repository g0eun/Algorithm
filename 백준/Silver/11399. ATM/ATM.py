N = int(input())
Pi = sorted(map(int, input().split()))

result = sum([Pi[idx] * (N - idx) for idx in range(N)])

print(result)
