import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.nbrs = set()
def mgc(root):
    if not root.nbrs:
        return 0
    else:
        ans = -sys.maxsize
        for i in list(root.nbrs):
            ans = max(ans,mgc(i))
        return ans+1
class Solution:
    def MaxmimumLength(self, nums):
        sets = []
        nodes = []
        maxi = max([max(i) for i in nums])
        for i in range(-1,maxi+1):
            nodes.append(Node(i))
        for i in nums:
            sets.append(set(i))
        n = len(nums)
        for i in range(n):
            temp = nums[i]
            for j in temp:
                for k in range(n):
                    if k!=i:
                        if j+1 in sets[k]:
                            nodes[j].nbrs.add(nodes[j+1])
        ans = 1
        for i in nodes:
            ans = max(ans,mgc(i))
        return ans