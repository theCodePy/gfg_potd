import random
from tqdm import tqdm

### the main solution ###
#########################################

class Solution:
    def coin(self, arr):
        le_ = len(arr)
        if le_==1 :
            return arr[0]
        l = 0
        r = le_ - 1
        while l<r:
            if arr[l]>=arr[r]:
                l+=1
            else:
                r-=1
        return arr[l]


# ---------------------------------
########################################
## main solution 2 find the minimum of all####

class Solution:
    def coin(self, arr):
        ans = arr[0]
        for a in arr:
            ans = min(ans, a)
        return ans

# ---------------------------------
########################################

obj = Solution()
for i in tqdm(range(1000)):
    size = random.randint(1, 10**5)
    arr = []
    for i in range(size):
        arr.append(random.randint(1,10**6))
    obj.coin(arr)
