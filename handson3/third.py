def print_solid_rec(m,n):
    for i in range(m):
      for j in range(n):
        print('#',end='')
      print()

M = int(input('Enter M no of rows: '))
N = int(input('Enter N no of columns: '))

print_solid_rec(M,N)
