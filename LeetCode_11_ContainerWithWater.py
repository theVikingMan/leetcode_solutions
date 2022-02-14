
def maxArea(height):
    best = 0
    l = 0
    r = len(height) - 1

    while l < r:
        best = max(best, (min(height[l], height[r]) * (r - l)))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best



print(maxArea([1, 8, 6, 2, 5, 4, 3, 8, 7]))