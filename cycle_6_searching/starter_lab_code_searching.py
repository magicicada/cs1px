def iterative_binary_search_buggy1(my_list, value): 
    lo, hi = 0, len(my_list)-1 
    while lo < hi: 
        mid = (lo + hi) // 2 
        if my_list[mid] < value: 
            lo = mid + 1 
        elif value < my_list[mid]: 
            hi = mid - 1 
        else: 
            return mid 
    return -1 


def iterative_binary_search_buggy2(my_list, value): 
    lo, hi = 0, len(my_list)-1 
    while lo <= hi: 
        mid = (lo + hi) // 2 
        if my_list[mid] < value: 
            lo = mid + 1 
        elif value <= my_list[mid]: 
            hi = mid - 1 
        else: 
            return mid 
    return -1 


def iterative_binary_search_buggy3(my_list, value): 
    lo, hi = 0, len(my_list)-1 
    while lo <= hi: 
        mid = (lo + hi) // 2 
        if my_list[mid] <= value: 
            lo = mid + 1 
        elif value < my_list[mid]: 
            hi = mid - 1 
        else: 
            return mid 
    return -1 
