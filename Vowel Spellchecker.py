"""
This a solution for the problem from
https://leetcode.com/problems/vowel-spellchecker/

Here is the copy of the problem from leetcode:

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

"""
from collections import defaultdict
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vow='aeiou'
        def getAlldiff(st):
            output=[]
            for i in range(len(st)):
                if st[i] in vow:
                    output_temp=getAlldiff(st[i+1:])
                    for o in output_temp:
                        for v in vow:
                            output.append(st[:i]+v+o)
            if not output:
                if st in vow:
                    return ['']
                else :
                    output.append(st)
            return output
        def diff(s1,s2):
            count=0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
            return count

        set_Wrods=set(wordlist)
        map_words_to_index=defaultdict(int)
        for i,word in enumerate(wordlist):
            if word not in map_words_to_index:
                map_words_to_index[word]=i
        map_lower_to_original=defaultdict(set)
        for word in wordlist:
            map_lower_to_original[word.lower()].add(map_words_to_index[word])
        output=['' for l in queries ]
        for i ,query in enumerate(queries):
            if query in set_Wrods:
                output[i]=query
            elif map_lower_to_original.get(query.lower()) :
                min_index=min(map_lower_to_original[query.lower()])
                output[i]=wordlist[min_index]
            else:
                pot_match=getAlldiff(query.lower())
                words_index=[]
                for q in pot_match:
                    if map_lower_to_original.get(q):
                        for orig_word_index in map_lower_to_original.get(q) :
                            words_index.append(orig_word_index)
                if words_index:
                    output[i]=wordlist[min(words_index)]
                
        return output
                
