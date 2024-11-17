#https://www.spoj.com/CMI2020/status/CMI_01_42,juliarzymowska/ - do zrobienia a'la bfs'em

def skoczek(T, k, w, length): #tablica, kolumna, wiersz, długość drogi
    if w == len(T):
        return length

    if T[w+2][k+1] == 0 and w+2 < len(T) and k+1 < len(T):
        skoczek(T, k+1, w+2, length+1)
    elif T[w+2][k-1] == 0 and w+2 < len(T) and k-1 >= 0:
        skoczek(T, k-1, w+2, length+1)
    elif T[w+1][k+2] == 0 and w+1 < len(T) and k+2 < len(T):
        skoczek(T, k+2, w+1, length+1)
    elif T[w+1][k-2] == 0 and w+1 < len(T) and k-2 >=0:
        skoczek(T, k-2, w+1, length+1)

def zad112(T):
    l = len(T)
    ans = 0

    for i in range(l):
        temp = skoczek(T, i, 0, 0)
        ans = min(ans, temp)

    return ans

def main():
    T = [(0,0), (0,0), (0,0), (0,0)] #najpierw wiersz potem kolumna, rozmiar NxN
    print(zad112(T))

main()
'''
def zajecia(T, pos): # ma to sens, do napisania w domu
    if pos[1] == len(T) - 2:
        return 0
        
    moves = [(-2,1), (-1,2), (1,2), (2,1)]
    
    mini = float("inf") # definicja nieskonczonosci w pythonie
    for move in moves:    
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if T[new_pos[0]][new_pos[1]] == 0:
            a = zajecia(T, new_pos)
            if a < mini
                mini = a
    
    return mini + 1

def funkcja(T):
    arr = [*T, [1 for _ in range(len(T)] # bierze elementy T (tworzy jej kopię)
    
    #    T = [1,2]
    #    A = [*T, 3] B = [T, 3]
    #    T = [1,2,3] T = [[1,2], 3]
    
    
    for t in arr:
        t += [1, 1]
        
    for i in range(len(T)):
        a = solution(arr, (0, i))
        ans = min(ans, a)
        
    return ans
'''