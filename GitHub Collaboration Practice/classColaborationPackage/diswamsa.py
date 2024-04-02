#diswamsa.py
# Name: Smita Magar
# email:diswamsa@mail.uc.edu
# Assignment Number: Git hub collaboration practice
# Due Date:4/2/2024
# Course/Section:IS 4010/001
# Semester/Year:spring/2024
# Brief Description of the assignment: This assignment is creating a new module in project which we clone from github
# Brief Description of what this module does: we import print_companies from utils.py and invoke  in the 
# main module.
# Anything else that's relevant:
def diswamsa():
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6]  # Example input array
    if not nums:
        return 0
    
    # Initialize variables
    k = 0  # Pointer for the unique elements
    
    # Loop through the array
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    return k + 1
 
if __name__ == "__main__":
    #printing the function
    print(diswamsa())
