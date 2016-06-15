def fibonacci(x):

    fib_list = []
    f = 1
    i=0
   
    while i<x:
    	if i<=1:
    		 fib_list.append(f)
    		 
    	else:
    		f = fib_list[-1] + fib_list[-2]   #says that f = the sum of the last two f's in the series
        	fib_list.append(f)
        i+=1
        
    else:
    	return fib_list
        
print fibonacci(8)