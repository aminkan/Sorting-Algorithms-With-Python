

def sort(List):
    if len(List) == 1:
        return List
    else:
        middle = int(len(List) / 2)
        left = sort(List[0:middle]) """ sort the left part of the list """
        right = sort(List[middle:len(List)]) """ sort the right part of the list """
        sorted = merge(left, right) """ merge the sorted left part and the sorted right part """

        return sorted


def merge(left, right):
    List = []
    l, r = 0, 0
    nl = len(left)
    nr = len(right)
    while (l < nl and r < nr):
        if left[l] > right[r]:
            List.append(right[r])
            r += 1
        else:
            List.append(left[l])
            l += 1
    while l < nl:
        List.append(left[l])
        l += 1
    while r < nr: 
        List.append(right[r])
        r += 1
    return List

