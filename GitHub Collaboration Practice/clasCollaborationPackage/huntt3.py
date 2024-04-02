#huntt3.py
#********************************************************************************************************************************************************************************
# Name: Trevor Hunt                                                                                                                                                             *
# email: huntt3@mail.uc.edu                                                                                                                                                     *
# Assignment Number: Collaboration                                                                                                                                             *
# Due Date: 04/02/2024                                                                                                                                                          *
# Course/Section: IS4010-001                                                                                                                                                    *
# Semester/Year: Spring 2024                                                                                                                                                    *
# Brief Description of the assignment: Demonstrates collaboration using github                                                                                              *
#                                                                                                                                                                               *
# Brief Description of what this module does: Creates function for leetcode problem                                                 *
# Citations: https://leetcode.com/rahulvarma5297/, https://leetcode.com/problems/remove-duplicates-from-sorted-array/   *
# Anything else that's relevant:                                                                                                                                                *
#********************************************************************************************************************************************************************************\

def removeDuplicates():
    '''
    removes duplicates from sorted list and prints new list
    @param: none
    @return: none
    '''
    nums = [0,0,1,1,1,2,2,3,3,4]
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    print(nums[:j])
    
if __name__ == "__main__":
    removeDuplicates()