
class Solution:
    """class representing a practise"""

    def __init__(self) -> None:
        pass

    def reverse_str(self, text: str) -> str:
        """LeetCode 344.翻转字符串"""
        text_list = list(text)
        left, right = 0, len(text_list)-1
        while left < right:
            temp = text_list[left]
            text_list[left] = text_list[right]
            text_list[right] = temp
            left += 1
            right -= 1
        res = ''.join(text_list)
        return res



if __name__ == "__main__":
    text_str = "hello"
    s = Solution()
    res = s.reverse_str(text_str)
    print(res)
