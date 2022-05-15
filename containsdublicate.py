class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False
