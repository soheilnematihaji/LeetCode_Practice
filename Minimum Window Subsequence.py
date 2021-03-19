"""
This a solution for the problem from
https://leetcode.com/problems/minimum-window-subsequence/

Here is the copy of the problem from leetcode:

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

"""

""" This solution is correct but it doesn't have the bestt timing. It will result in Time Limit Exceeded  """

""" TO DO:
        Make it more efficient
    """
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def minWindowWithIndex(S,T):
            length_s=None
            for j in range(len(S)-1,-1,-1):
                if S[j] == T[-1]:
                    length_s=j+1
                    break
            if not length_s:
                return None
            dynamic_min=[[None for j in range(len(T))] for i in range(length_s)]
            for j in range(len(T)-1,-1,-1):
                for i in range(length_s-1,-1,-1):
                    if S[i]==T[j]:
                        if j==len(T)-1:
                            dynamic_min[i][j]= (i,i+1)
                            continue
                        if i <length_s-1:
                            minText=dynamic_min[i+1][j+1]
                        else:
                            minText=None
                        if j==0 and  i<length_s-1:
                            minText2=dynamic_min[i+1][j]
                        else:
                            minText2=None
                    elif i<length_s-1:
                        minText2=dynamic_min[i+1][j]
                        minText=None
                    else:
                        minText=None
                        minText2=None
                    if minText:
                        if not minText2:
                            dynamic_min[i][j]= (i,minText[1])
                        else:
                            if j==0:
                                if minText2[1]-minText2[0]>=minText[1]-i:
                                    dynamic_min[i][j]= (i,minText[1])
                                else:
                                    dynamic_min[i][j]= minText2
                            else:
                                if minText2[1]-i>=minText[1]-i:
                                    dynamic_min[i][j]= (i,minText[1])
                                else:
                                    dynamic_min[i][j]= minText2
                    elif minText2:
                        dynamic_min[i][j]= minText2
            return dynamic_min[0][0]
        interval=minWindowWithIndex(S,T)
        if interval:
            return S[interval[0]:interval[1]]
        else:
            return ''
        

        
