import time 

def fibonacci(N):
    if((N== 0) or (N==1)):
       return N
    else:
       return fibonacci(N-1) + fibonacci(N-2)
    

def get_time(N):
    t0 = time.time()
    fibonacci(N)
    t1 = time.time() - t0
    return t1

for i in range(0, 36):
    print i , get_time(i)

    
