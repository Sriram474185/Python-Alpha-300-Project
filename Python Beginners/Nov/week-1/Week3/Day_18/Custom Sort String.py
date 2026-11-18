def qsort(arr, rank):
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left = [x for x in arr[1:] if rank.get(x, 26) < rank.get(p, 26)]
    right = [x for x in arr[1:] if rank.get(x, 26) >= rank.get(p, 26)]
    return qsort(left, rank) + [p] + qsort(right, rank)

def customSortString(order: str, s: str) -> str:
    rank = {c: i for i, c in enumerate(order)}
    return "".join(qsort(list(s), rank))
