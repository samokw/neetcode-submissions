class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # the idea here is to use a suffix max approach
        # we also need to keep a temp varible where we hold the current number
        # we start the array with the value of -1 because it doesn't have a right element
        # then we update the max as we go, comparing the current number and the max_val
        max_val = -1
        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = max_val
            max_val = max(temp, max_val)
        return arr