### 45. Rotate List (Medium)
#**Description:** Rotate list right by k positions.
#**Example Input:** [1,2,3,4,5], k=2
#**Expected Output (blueprint):** [4,5,1,2,3]
###
def rotate_right(nums, k):
    k = k % len(nums)        # handle k larger than length
    return nums[-k:] + nums[:-k]

print(rotate_right([1,2,3,4,5], 2))   # Output: [4,5,1,2,3]
