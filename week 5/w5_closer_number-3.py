def nearest_number(lst, target):
    return min(lst[:n], key=lambda x: abs(x-target))
n = int(input())
l = list(map(int, input().split()))
target = int(input())
print(nearest_number(l, target))
