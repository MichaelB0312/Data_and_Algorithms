from collections import deque
from typing import Optional, List, Tuple, Set, Dict, Any, Union


'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"],
 then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
 "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
 
Return an array of the starting indices of all the concatenated substrings in s.
 You can return the answer in any order
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        out_list = []
        subwords: Dict[str, int] = {}

        for word in words:
            subwords[word] = 0

        for i in range(0, len(s)-len(words)*len(words[0]), len(words[0])):
            curr_substring = s[i:i+len(words)*len(words[0])]
            cnt = 0
            k = 0
            while (k < len(words)*len(words[0])):
                if (curr_substring[k:k+len(words[0])] in subwords) and (not subwords[curr_substring[k:k+len(words[0])]]):
                    subwords[curr_substring[k:k+len(words[0])]] = 1
                    cnt += 1
                    k += len(words[0])

                else:
                    break

            subwords = dict.fromkeys(subwords, 0)
            if cnt == len(words):
                out_list.append(i)

        return out_list

sol = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(sol.findSubstring(s,words))

