t = [[1,2,3], [1,5,6], [2,8,9]]
# do rozkminy
def zad117(t : list):
   n = len(t)
   max_l = 0 #max length ciagu fib

   for i in range(n-2): #n-1, bo ciag bedzie krotszy niz co najmniej 3
       for j in range(n-2): #n-2, bo ciag bedzie krotszy niz co najmniej 3
           #szybciej sprawdzić czy 2 kolejne sa suma niz czy t[i][j] nalezy do fibonacciego

           # sprawdzanie malejąco
           first = t[i][j]
           second = t[i+1][j+1]
           third = t[i+2][j+2]
           if first <= second and third == first + second and fib(first, second):
                max_l = 3
                while i+3 < n and j+3 < n and t[i+2][j+2] == t[i][j] + t[i+2][j+2]: #żeby nie wyjść poza rozmiar tablicy
                   first, second, third = second, third, t[i+3][j+3]
                   i += 1
                   j += 1
                   if third != first + second:
                        return max_l
                   max_l += 1
                # end while
                return max_l

def fib(x : int, y : int): #sprawdzanie czy first i second to liczby fibonacciego
   a, b = 0, 1
   while a < x:
      if a == x and b == y:
         return True
      else:
         a, b = b, a+b
   return False
def main():
    #n = int(input())
    print(zad117(t))
main()