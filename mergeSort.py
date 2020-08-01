def mergeSortedLists(listA, listB):
    result = []
    while len(listA) > 0 and len(listB) > 0:
        if listA[0] < listB[0]:
            result.append(listA.pop(0))
        else:
            result.append(listB.pop(0))
    result = result + listA + listB
    return result

def mergeSort(list):
    if len(list) <= 1:
        return list
    half = round(len(list)/2)
    listA = list[0:half]
    listB = list[half:len(list)]
    return mergeSortedLists(mergeSort(listA), mergeSort(listB))
