principal = input("Enter the Principal amount: ")
rate= input("Enter the rate of interest: ")
time= input("Enter the time (in Years) : ")

principal = float(principal)
rate = float(rate)
time = float(time)

interest = (principal*rate*time)/100    # interest calculation formula

print("The Interest ino the Principle: ", interest)