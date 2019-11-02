"""
No.5
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
1. 最长公共子串：反转字符串，然后判断寻找公共子串，并判断是否是回文
2. 暴力法：从长到短，讲所有可能的子串列出，并判断是否为回文，O(n^3)
3. 动态规划：回文左右字母相同，因此可以从这个特性出发一步步寻找左右相同的子串
4. 中心扩展算法：利用回文镜像原理，从中心展开，2n-1个中心
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩展算法
        - time: 1160 ms
        - mens: 13.9 MB
        """
        if s is None or len(s) < 0: return ""
        start = 0
        end = 0
        for i in range(0,len(s)):
            len_odd = expandAroundCenter(s,i,i)
            len_even = expandAroundCenter(s,i,i+1)
            length = max(len_odd,len_even) # length最小为1
            if length > end - start:
                start = i - (length-1)//2
                end = i + length //2
        print(start,end)
        return s[start:end+1]

def expandAroundCenter(s,L,R):
    while(L>=0 and R<len(s) and s[L] == s[R]):
        L=L-1
        R=R+1
    return R-L-1 # 退出条件是s[L]!=s[R]
    
if __name__ == "__main__":
    s = "babad"
    m = Solution()
    o = m.longestPalindrome(s)
    print(o)
