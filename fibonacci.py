fibonacci = [0,1]

for i in range(7):
    next_num = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(next_num)

print("The first ten number of the Fibonacci sequence are: " + str(fibonacci))