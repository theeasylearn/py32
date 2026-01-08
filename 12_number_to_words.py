#write a program to convert given 2 digit amount into words
# input : 75 output : seven five 
# task seventy five
amount = input("Enter amount")
#convert amount into integer
amount = int(amount) 
#i want both digits in different variable 
last = amount % 10 # 5
# print(last)
first = amount // 10 # 7
# print(first)
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
#          0    1       2    3       4      5      6       7       8       9
print(words[first]," ",words[last])
