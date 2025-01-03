class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        for i,citation in enumerate(citations):
            if length - i <= citation:
                return length - i
        return 0