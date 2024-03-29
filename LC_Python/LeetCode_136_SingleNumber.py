# -------------   Bit manipulation ------------- #

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

print(singleNumber([2,2,1]))

#  ------------ Extra Space ------------ #

def singleNumber(nums):
	mapping = {}
	for num in nums:
			if num not in mapping:
					mapping[num] = 1
			else:
					mapping[num] += 1
	for key in mapping:
			if mapping[key] == 1:
					return key