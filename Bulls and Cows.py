"""
This a solution for the problem from
https://leetcode.com/problems/bulls-and-cows/

Here is the copy of the problem from leetcode:
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        map_digit_to_count_secret={i:0 for i in range(10)}
        map_digit_to_count_guess={i:0 for i in range(10)}
        bulls=0
        for a,b in zip(secret,guess):
            if a ==b :
                bulls+=1
            map_digit_to_count_secret[int(a)]+=1
            map_digit_to_count_guess[int(b)]+=1
        cows=0
        for i in range(10):
            cows+= min(map_digit_to_count_secret[i],map_digit_to_count_guess[i])
        return str(bulls)+'A'+str(cows-bulls)+'B'
