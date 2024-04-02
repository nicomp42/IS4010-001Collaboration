# laughlcd.py

# LeetCode Function Number: 136

def laughlcd(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res ^= nums[i]
    return res

# Example usage
nums1 = [2, 2, 1]
print("Element occurring once is:", laughlcd(nums1))  # Output: 1

nums2 = [4, 1, 2, 1, 2]
print("Element occurring once is:", laughlcd(nums2))  # Output: 4

nums3 = [1]
print("Element occurring once is:", laughlcd(nums3))  # Output: 1