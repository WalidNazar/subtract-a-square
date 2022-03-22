#!/usr/bin/python
#text.upper()
print('Welcome To Game')
x=str(input("Do you want to start the game ? \n press (yes) or (no) \n "))
if x==('yes'):   
   sum=0
   print("\n"'First person to collect 100 coins wins'"\n")
if x==('no'):
    print('see you, later')
    x=0
    exit   

while x :
      w=int(input('player 1 choose number:'))
      if w==1 or w==4 or w==9 or w==16 or w==25 or w==36 or w==49 or w==64 or w==81 :
                         sum =sum+w
      else :
          print ("error choose anthore number")
      if sum==100 :
               print('you win, congratulations')
               break
      if sum>100:
          print ("you lost good luck next time")
          break
      y=int(input('player 2 choose number:'))       
      if y==1 or y==4 or y==9 or y==16 or y==25 or y==36 or y==49 or y==64 or y==81 :
                           sum =sum+y
      else :
          print ("error ,try again ")
      if sum==100 :
            print('you win, congratulations') 
            break
      if sum>100:
         print ("you lost good luck next time")
         break
     



