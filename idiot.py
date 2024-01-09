while True:
 number=int(input("Enter Any Number between 1500 to 2500:"))
 if number >= 1500:
  if number <= 2500:
   if number%7 == 0:
    if number%5 == 0:
     print("This {} is Divisible by 7".format(number),end=" ")
     print("and Multiples of five is:{}".format(number))
     break
   else:
    print("This {} is Not Divisible by 7".format(number))
    break