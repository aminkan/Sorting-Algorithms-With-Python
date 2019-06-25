
def sort(List):
    for i in range(len(List) - 1):
        for j in range(len(List) - i - 1):
            if List[j] > List[j+1]:
                flag = List[j+1]
                List[j+1] = List[j]
                List[j] = flag
    
    return List

