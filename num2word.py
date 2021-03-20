number=[" ","one","Two","Three","four","Five","Six","Seven","eight","nine"]
nty=[" "," ","Twenty","Thirty","fourty","Fifty","Sixty","Seventy","eighty","ninty"]
tens=["ten"," eleven","twelve","thirteen","fourteen","Fifteen","Sixteen","Seventeen","eighteen","ninteen"]
n=int(input("enter a number"))
if n>99999:
 print("cant solve for more than 5 digits")
else:
 d=[0,0,0,0,0,]
 i=0
 while n>0:
  d[i]=n%10
  i+=1
  n=n//10
 num=""
 if d[4]!=0:
   if(d[4]==1):
     num+=tens[d[3]]+" thousands "
   else:
     num+=nty[d[4]]+" "+number[d[3]]+" thousands "
 else:
   if d[3]!=0:
    num+=number[d[3]]+" thousands "
 if d[2]!=0:
   num+=number[d[2]]+" Hundred "
 if d[1]!=0:
   if(d[1]==1):
     num+=tens[d[0]]
   else:
     num+=nty[d[1]]+" "+number[d[0]]
 else:
   if d[0]!=0:
    num+=number[d[0]]
 print(num)
   
  
  
