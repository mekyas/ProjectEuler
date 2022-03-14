def prisonAfterNDays(cells, N: int):
        for n in range(N):
            old = [c for c in cells]
            for i in range(8):
                if i == 0 or i ==7:
                    cells[i]=0
                elif old[i-1]==old[i+1]:
                    cells[i]=1
                else:
                    cells[i]=0
        return cells

print(prisonAfterNDays([0,1,0,1,1,0,0,1], 7))