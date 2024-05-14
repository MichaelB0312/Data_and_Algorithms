from typing import Optional, List, Tuple, Set, Dict, Any, Union

'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window.
  If there is no such substring, return the empty string "".
  
  Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''
class Solution:

    def __init__(self):
        self.correct_chars = 0
        self.t_dict = {}
    def minWindow(self, s: str, t: str) -> str:
        # build dict for t
        for i in range(len(t)):
            if t[i] in self.t_dict:
                self.t_dict[t[i]] += 1
            else:
                self.t_dict[t[i]] = 1

        l_ptr = 0
        r_ptr = 0

        # first advance r_ptr till we get legal substr
        curr_dict = {}
        while r_ptr < len(s) and self.correct_chars < len(self.t_dict):
            if s[r_ptr] in self.t_dict:
                if s[r_ptr] in curr_dict:
                    curr_dict[s[r_ptr]] += 1
                else: curr_dict[s[r_ptr]] = 1
                if curr_dict[s[r_ptr]] == self.t_dict[s[r_ptr]]:
                    self.correct_chars += 1
            r_ptr += 1

        if len(curr_dict) < len(self.t_dict):
            return ""

        for key in curr_dict:
            if curr_dict[key] < self.t_dict[key]:
                return ""

        min_substr = s[l_ptr:r_ptr]

        # Now,  try to get smaller substr
        while r_ptr <= len(s):

            while (s[l_ptr] not in self.t_dict or curr_dict[s[l_ptr]] > self.t_dict[s[l_ptr]]) and self.correct_chars == len(self.t_dict):  #leagal substr, start increment l
                if s[l_ptr] in self.t_dict:
                    curr_dict[s[l_ptr]] -= 1
                l_ptr += 1
                min_substr = s[l_ptr:r_ptr]

            if l_ptr < len(s) and s[l_ptr] in self.t_dict:
                self.update_dict(chars_dict=curr_dict, curr_char=s[l_ptr], l_r='l')

            l_ptr += 1

            r_ptr += 1
            if r_ptr<=len(s) and s[r_ptr-1] in self.t_dict:
                self.update_dict(chars_dict=curr_dict, curr_char=s[r_ptr-1], l_r='r')

        return min_substr

    def update_dict(self, chars_dict, curr_char, l_r:str):
        if curr_char in chars_dict:
            if l_r == 'l':
                chars_dict[curr_char] -= 1
            if l_r == 'r':
                chars_dict[curr_char] += 1
        else:
            chars_dict[curr_char] = 1

        if chars_dict[curr_char] == self.t_dict[curr_char] - 1:
            self.correct_chars -= 1
        if chars_dict[curr_char] == self.t_dict[curr_char]:
            self.correct_chars += 1




sol = Solution()
s = "a"
t = "aa"
print(sol.minWindow(s,t))


