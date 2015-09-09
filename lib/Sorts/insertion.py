def insertion(a,start=0,end=None):
    if end == None:
        end = len(a) - 1
    for i in range(start+1,end+1):
        if a[i-1] > a[i]:
            x = a[i]
            j = i - 1
            while j > start and a[j-1] > x:
                j -= 1
            a[j+1:i+1] = a[j:i]
            a[j] = x

