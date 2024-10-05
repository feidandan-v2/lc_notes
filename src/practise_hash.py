from typing import List


class HashSolution1(object):
    """有效字母异位词"""
    def func(self, s1:str, s2:str) -> bool:
        alpha_nums = [0] * 26
        for i in s1:
            alpha_nums[ord(i) - ord('a')] += 1
        for j in s2:
            alpha_nums[ord(j) - ord('a')] -= 1
        # if sum(alpha_nums) == 0:     # 这样不行，有在不同位置的 -1 和 1，也可能会等于0
        for k in alpha_nums:
            if k != 0:
                return False
        return True


class HashSolution2():
    """两个数组的交集"""
    def func(self, nums1:list, nums2:list) -> list:
        nums_dict = {}
        nums_set = set()
        for i in nums1:
            nums_dict[i] = nums_dict.get(i,0)+1
        for j in nums2:
            if j in nums_dict:
                nums_set.add(j)
        return list(nums_set)



class HashSolution3():
    """快乐数"""
    def func(self, n:int) -> bool:
        num_set = set()
        while n !=1:
            num_set.add(n)
            square_sum = self.get_num(n)
            n = square_sum
            if n in num_set:
                return False
        return True

    def get_num(self, n: int) -> int:
        num_str = str(n)
        num_square_sum = 0
        for num_i in num_str:
            num_square_sum += int(num_i) **2
        return num_square_sum



class HashSolution4():
    """两数之和"""
    def func(self, nums:List[int], target:int) -> list[int]:
        record_dict = {}
        for i, i_num in enumerate(nums):
            if target - i_num in record_dict:
                return [i, record_dict[target - i_num]]
            else:
                record_dict[i_num] = i
        return



class HashSolution5():
    """赎金信，lc383"""
    def func(self, ransom:str, magazine:str) -> bool:
        record_dict = dict()
        for i in magazine:
            record_dict[i] = record_dict.get(i, 0) +1
        print(record_dict)
        for j in ransom:
            if j not in record_dict:
                return False
        return True
    # 以上不能覆盖所有case，比如 'aaa', 'aab'

    def func1(self, ransom:str, magazine:str) -> bool:
        record_nums = [0]*26
        for i in magazine:
            record_nums[ord(i)-ord('a')] +=1
        for j in ransom:
            record_nums[ord(j)-ord('a')] -=1
        print(record_nums)
        for k in record_nums:
            if k < 0:
                return False
        return True



if __name__ == '__main__':
    # v1 = [1,2,3,4,5,6]
    # s1 = 'rat'
    # s2 = 'car'
    # A = HashSolution1()
    # res1 = A.func(s1, s2)
    # print(res1)

    # nums1 = [1,2,2,1,3]
    # nums2 = [2,2,3]
    # B = HashSolution2()
    # res2 = B.func(nums1, nums2)
    # print(res2)

    # n = 20
    # C = HashSolution3()
    # res3 = C.func(n)
    # print(res3)

    # nums = [2,7,1,10]
    # target = 9
    # D = HashSolution4()
    # res4 = D.func(nums, target)
    # print(res4)

    ransom = 'aaa'
    magazine = 'aab'
    E = HashSolution5()
    res5 = E.func(ransom, magazine)
    print(res5)
    res5_1 = E.func1(ransom, magazine)
    print(res5_1)
