class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Approach 1 - BF - O(n+(n+m)log(n+m)) and O(1)
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        
        # Approach 2 - BF Better - use third array - O(2*(m+n)) and O(m+n)
        
        # Approach 3 - Optimal 1 - Use 2 pointer - O(min(n,m)+n) and O(1) - NA for this question
        
        # Approach 4 - Optimal 2 - Gap method - O((n+m)log(n+m)) and O(1) - NA for this question
        