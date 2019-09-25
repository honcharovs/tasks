def IsPointInSquare(x, y):
    print("YES" * ((-1 <= x <= 1) and (-1 <= y <= 1)) +
          ("NO" * ((x < -1) or (x > 1) or (y < -1) or (y > 1))))


x = float(input())
y = float(input())
IsPointInSquare(x, y)
