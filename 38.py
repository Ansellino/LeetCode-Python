class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generates the n-th element of the count-and-say sequence.

        Args:
            n: The index of the element to generate.

        Returns:
            The n-th element of the count-and-say sequence.
        """

        if n == 1:
            return "1"

        prev_say = self.countAndSay(n - 1)
        curr_say = ""
        count = 1

        for i in range(1, len(prev_say)):
            if prev_say[i] == prev_say[i - 1]:
                count += 1
            else:
                curr_say += str(count) + prev_say[i - 1]
                count = 1

        curr_say += str(count) + prev_say[-1]

        return curr_say

    
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            # original
            # s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
            
            # decomposed
            v = '' # accumulator string
            # iterate the characters (digits) grouped by digit
            for digit, group in itertools.groupby(result):
                count = len(list(group)) # eg. the 2 in two 1s 
                v += "%i%s" % (count, digit) # create the 21 string and accumulate it
            result = v # save to result for the next for loop pass

        # return the accumulated string
        return result
'''
