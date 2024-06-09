
class Solution():
    """209 长度最小子数组"""
    def least_length_subarray(self, nums: list, val: int) -> list:
        fast, slow = 0, 0
        least_len = len(nums)
        for fast in range(0, len(nums)+1):
            if sum(nums[slow:fast]) > val:
                while sum(nums[slow:fast]) >= val:
                    slow += 1
                least_len = min(least_len, fast-slow+1)
        return least_len


if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    val = 7
    solution = Solution()
    res1 = solution.least_length_subarray(nums, val)
    print(res1)

