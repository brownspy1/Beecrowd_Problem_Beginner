def search(nums: [int], target: int):
    # n is the size of the array 'nums'

    n = len(nums) - 1

    # Initialising two variables

    # 's' and 'e'

    s = 0

    e = n - 1

    while s <= e:

        # Initializing the variable 'mid'

        mid = (s + e) >> 1

        # If the current index's value is equal to

        # target, we will return the current index

        if nums[mid] == target:

            return mid

        # If the value is greater than target,

        # we will decrease the value of 'e'

        elif nums[mid] > target:

            e = mid - 1

        # Otherwise, we will increase the value

        # of 's'

        else:

            s = mid + 1

    # If we didn't find anything, we will return -1.

    return -1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
target = int(input())
print(search(arr, target))