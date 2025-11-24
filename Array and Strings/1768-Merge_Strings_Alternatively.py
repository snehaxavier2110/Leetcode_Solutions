class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        '''final=[]
        i=0
        j=0
        n=len(word1)
        m=len(word2)
        while i<n or j<m:
            if i<n:
                final+=word1[i]
                i+=1
            if j<m:
                final+=word2[j]
                j+=1
        return "".join(final)'''
        result=[]
        minl=min(len(word1),len(word2))
        for i in range(minl):
            result.append(word1[i])
            result.append(word2[i])   
        if len(word1)>len(word2):
            result.append(word1[minl:])
        elif len(word2)>len(word1):
            result.append(word2[minl:])    
        return ''.join(result)             
          
"""
Approach 1: Two Pointers
Intuition
There are numerous ways in which we can combine the given strings. 
We've covered a few of them in this article.

An intuitive method is to use two pointers to iterate over both strings. 
Assume we have two pointers, i and j, with i pointing to the first letter of word1 and j pointing to the first letter of word2. 
We also create an empty string result to store the outcome.

We append the letter pointed to by pointer i i.e., word1[i], and increment i by 1 to point to the next letter of word1.
Because we need to add the letters in alternating order, next we append word2[j] to result. We also increase j by 1.

We continue iterating over the given strings until both are exhausted.
We stop appending letters from word1 when i reaches the end of word1, and we stop appending letters from word2' when j reaches the end of word2.

Algorithm
1. Create two variables, m and n, to store the length of word1 and word2.
2. Create an empty string variable result to store the result of merged words.
3. Create two pointers, i and j to point to indices of word1 and word2. We initialize both of them to 0.
4. While i < m || j < n:
   4.1 If i < m, it means that we have not completely traversed word1. 
       As a result, we append word1[i] to result. We increment i to point to next index of word1.
   4.2 If j < n, it means that we have not completely traversed word2.
       As a result, we append word2[j] to result. We increment j to point to next index of word2.
Return result.


Complexity Analysis
Here, m is the length of word1 and n is the length of word2.

Time complexity: O(m+n)

We iterate over word1 and word2 once and push their letters into result. It would take O(m+n) time.
Space complexity: O(1) or O(m+n)

Without considering the space consumed by the input strings (word1 and word2) and the output string (result), we do not use more than constant space.
"""