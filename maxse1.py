def findzero(A):
    count = 0
    max_count = 0 
    left = 0
    max_index = -1
    prev_index = -1
    for i in range(len(A)):
        if A[i]==0:
            count+=1
            prev_index = i
        if(count == 2):
            while A[i]:
                left = left+1
            left = left+1

        count =1

        if i-left +1 > max_count:
            max_count = i-left+1
            max_index = prev_index
    return max_index

    


if __name__ == '__main__':
    A = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    index = findzero(A)
    if index != -1:
        print("Index to be replaced is", index)
    else:
        print("Invalid input")