# input : array nums of size n
# output : return the closest number to 0

def findClosestNumber(self,nums):
    closest=nums[0]
    for x in nums:
        if abs(x) < abs(closest):
            closest = x
    if closest < 0  and abs(closest) in nums:
        return abs(closest)
    else:
        return closest   
    
'''
----Intuition: 
Find the distances and store the least value in the nums to save it as closest number to 0. then check for any base conditions to be satisfied.

----Approach
1. Save the first value of nums as the closest
2. Iterate over the nums to look for least value other than the current closest, if so replace then with the new least value.
( Note: Here the absolute values are compared, otherwise higher negative value will be the closest but it is not.)
3. If both negative and positive of a number appears as the closest then its absolute value is to be returned.
4. Else we need to send the closest value store in variable closest.

----Complexity
1. Time complexity: O(2n) == O(n)
One for the for loop and one for the loop up of smallest in nums.

2. Space complexity: O(1)
There is no additional memory used other than input list.
'''     