def uniquePaths(nums:list[int])->int:
    nums[0][0]=1
    n=len(nums)
    for i in range(n):
        for j in range(len(nums[i])):
            if i==0 and j==0:
                continue
            if nums[i][j]==1:
                nums[i][j]==0
                continue
            else:
                if i==0:
                    nums[i][j]=nums[i][j-1]
                elif j==0:
                    nums[i][j]=nums[i-1][j]
                else:
                    nums[i][j]=nums[i-1][j]+nums[i][j-1]
    return nums




print(uniquePaths([[0,0,0], [0,1,0], [0,0,0]]))
