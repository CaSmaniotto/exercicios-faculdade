# insertionsort
def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x

ls = [3,1,2,5,6,8,4]
insertion_sort(ls)