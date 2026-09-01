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
                prevsecs = set()
                while l < r:
                    newsom = nums[l] + nums[r]
                    if nums[l] not in prevsecs:
                        if newsom == -newtarg:
                            agg.append([v, nums[l], nums[r]])
                            prevsecs.add(nums[l])
                            l +=1
                        elif newsom < -newtarg:
                            l+=1
                        else:
                            r -=1
                    else:
                        l+=1
        return agg
        