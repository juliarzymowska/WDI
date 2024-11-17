n = 7

t = [[1 for _ in range(n)] for _ in range(n)]

ind = 0 #indentation

while ind <= n//2:
    for i in range(0+ind,n-ind): #wiersz 0, kolumna i
        if not(i == 0 and ind == 0):
            t[0+ind][i] = t[0+ind][i-1] + 1
    for i in range(1+ind,n-ind): #wiersz i, kolumna n-2
        t[i][n-1-ind] = t[i-1][n-1-ind] + 1
    for i in range(n-2-ind, -1+ind, -1): #wiersz n-2, kolumna i
        t[n-1-ind][i] = t[n-1-ind][i+1] + 1
    for i in range(n-2-ind, 0+ind, -1): # kolumna 0, wiersz i
        t[i][0+ind] = t[i+1][0+ind] + 1

    ind += 1

for wiersz in t:
    print(wiersz)