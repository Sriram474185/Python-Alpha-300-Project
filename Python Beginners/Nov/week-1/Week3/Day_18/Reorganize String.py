def qsort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left = [x for x in arr[1:] if x >= p]
    right = [x for x in arr[1:] if x < p]
    return qsort(left) + [p] + qsort(right)


def reorganizeString(s: str) -> str:
    n = len(s)
    pairs = qsort([(s.count(c), c) for c in set(s)])

    if pairs[0][0] > (n + 1) // 2:
        return ""

    chars = [c for count, c in pairs for _ in range(count)]
    res = [""] * n
    res[::2], res[1::2] = chars[: (n + 1) // 2], chars[(n + 1) // 2 :]
    return "".join(res)
