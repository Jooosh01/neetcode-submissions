class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        prevheads = set()
        agg = []
        nums.sort()
        for i, v in enumerate(nums):
            if v not in prevheads:
                prevheads.add(v)
                l = i+1
                r = len(nums)-1
                newtarg = 0 + v
                while l < r:
                    newsom = nums[l] + nums[r]
                    if newsom == -newtarg:
                        agg.append([v, nums[l], nums[r]])
                        l +=1
                        while nums[l] == nums[l-1] and l <r:
                            l+=1
                    elif newsom < -newtarg:
                        l+=1
                    else:
                        r -=1

        return agg
        