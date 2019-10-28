"""
No.1 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def twoSum(self, nums, target):
        """
        暴力解法
        - time: 5600 ms
        - men: 14.8 MB
        """
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
    
    def twoSum_1(self, nums, target):
        """
        找num2=target-num1是否在list中，这样只计算一次
        - time: 1260 ms
        - men: 14.8 MB
        """
        n = len(nums)
        for i in range(0,n-1):
            num2 = target-nums[i]
            if num2 in nums:
                if (nums.count(num2) == 1)&(num2 == nums[i]): #避免num2是num1本身
                    continue
                else:
                    j = nums.index(num2,i+1)
                    break
        if j>0:
            return [i,j]
        else:
            return []

    def twoSum_2(self, nums, target):
        """
        找num2从之后的nums查找
        - time: 1076 ms
        - men: 14.7 MB
        """
        n = len(nums)
        for i in range(0,n-1):
            num2 = target-nums[i]
            temp = nums[i+1:] # 之后的nums，这里是引用不会赋值
            if num2 in temp:
                j = nums.index(num2,i+1)
                break
        if j>0:
            return [i,j]
        else:
            return []
    
    def twoSum_3(self, nums, target):
        """
        字典模拟哈希求解
        - time: 72 ms
        - men: 14.9 MB
        """
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target-num) is not None:
                return [i,hashmap.get(target-num)]
            hashmap[num] = i # 建立 num:index 字典


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    s = Solution()
    print(s.twoSum(nums,target))