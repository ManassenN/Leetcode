def searchRange(nums, target):
    error = [-1, -1]
    result = []

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            if nums[mid - 1] != target and nums[mid - 1]:
                result.append(mid)
                break
            else:
                right = mid - 1
                continue
        if nums[mid] > target:
            right = mid - 1
            continue
        else:
            left = mid + 1
            continue

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target and nums[mid + 1]:
            if nums[mid + 1] != target:
                result.append(mid)
                break
            else:
                left = mid + 1
                continue
        if nums[mid] > target:
            right = mid - 1
            continue
        else:
            left = mid + 1
            continue

    if len(result) == 0:
        return error
    else:
        return result


nums = [1]
print(searchRange(nums,1))