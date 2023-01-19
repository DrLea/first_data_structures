def maxSubArray(array,size):
     
    max_so_far = int(array[0])
    max_ending_here = 0
     
    for i in range(0, size):
        max_ending_here = max_ending_here + int(array[i])
        if max_ending_here < 0:
            max_ending_here = 0
         

        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
             
    return max_so_far
    
array = []
for i in range(8):
    array.append(input())
print(maxSubArray(array, len(array)))


