
nums = [2,9,11,7]
target = 9
def twoSums( nums ,target ):
    n = len(nums)
    for i in range(n) :
        for j in range( i+1 , n ) :
            if nums[i] + nums[j] == target:
                return [i,j]
    return []


result = twoSums( nums , target)
print( result)

## range 函数

