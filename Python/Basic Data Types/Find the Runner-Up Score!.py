if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    ls =  sorted(l)
    
    for i in range(n-2,-1,-1):
        if ls[i] != ls[n-1]:
            print(ls[i])
            break