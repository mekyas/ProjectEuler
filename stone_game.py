def winnerSquareGame(n: int) -> bool:
        from math import sqrt
        square = []
        for i in range(1, int(sqrt(n))+1):
            square.append(i**2)
        def winner(x, alice=True):
            if x == 1:
                if alice:
                    return True
                else:
                    return False
            else:
                return all([winner(x-s, alice=not alice) for s in square if s<x])
        return winner(n, True)

print(winnerSquareGame(6))