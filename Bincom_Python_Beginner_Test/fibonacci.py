def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

    nterms = n

    # check if the number of terms is valid
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        #    print("Fibonacci sequence:")
        for i in range(nterms):
            fibo.append(i)
        print(fibo)
    print("the sum of the first 50 terms of a fibonacci sequence is: ", sum(fibo))
