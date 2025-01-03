class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total = []
        for op in operations:
            if op == "C":
                total.pop()
            elif op == "+":
                total.append(total[-1] + total[-2])
            elif op == "D":
                total.append(total[-1] * 2)
            else : total.append(int(op))
        return sum(total)