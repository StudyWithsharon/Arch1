print("Enter the Binary Number: ")
binary = int(input())

decimal = 0
i = 1
while binary!=0:
    rem = binary%10 #division by 10 giving the remainder
    decimal = decimal + (rem*i) #current remainder multiplied by the value of i
    i = i*2
    binary = int(binary/10) #removing the last digit by division

print(decimal)
