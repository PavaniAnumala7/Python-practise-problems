def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


A = list(map(int,input().split(" ")))

start = mid = 0
end = len(A)-1
pivot =1 

while mid<=end:
    
    if A[mid]<pivot:
        swap(A,start,mid)
        start +=1
        mid +=1
    elif (A[mid]>pivot):
        swap(A,end,mid)
        end -=1
        
    else:
        mid+=1
print(A)
        

       