class Solution:
    def findWinners(self, matches) :
        # write code here
        bracket = {}
    
        for winner, loser in matches:
            bracket[winner] = bracket.get(winner,0)
            bracket[loser] = bracket.get(loser,0) + 1

        zero_lose = [player for player, lose in bracket.items() if lose == 0]
        one_lose = [player for player, lose in bracket.items() if lose == 1] 

        zero_lose.sort()
        one_lose.sort()
        
        return [zero_lose, one_lose]
    
    '''
    class Solution:
    def findWinners(self, matches):
        bracket = {}

        for winner, loser in matches:
            bracket[winner] = bracket.get(winner, 0)
            bracket[loser] = bracket.get(loser, 0) + 1

        zero_lose = [player for player, lose in zip(bracket.keys(), bracket.values()) if lose == 0]
        one_lose = [player for player, lose in zip(bracket.keys(), bracket.values()) if lose == 1]

        zero_lose.sort()
        one_lose.sort()

        return [zero_lose, one_lose]
    '''