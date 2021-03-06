# O(N) 1
def uniqueTwoSum(nums, target):
  ans, comp = set(), set()
  for n in nums:
    c = target-n
    if c in comp:
      res = (n, c) if n > c else (c, n)
      if res not in ans:
        ans.add(res)
    comp.add(n)
  return len(ans)

# O(N)3
def uniquePairs(nums, target):
    ans = set()
    comp = set()
    for num in nums:
        c = target - num
        if c in comp:
            res = (num, c) if num > c else (c, num)
            ans.add(res)       
        comp.add(num)
    return len(ans)
  
# O(N) 2
def uniquePairs(nums, target):
    res = {}
    out = set()

    for index, value in enumerate(nums):
        if target - value in res:
            out.add((value, target-value))
        else:
            res[value]=index

    return len(out)
  
  
