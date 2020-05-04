#leet code question maximum array
#brute force
n = [2, 7, 11]
def maximumsubarray(n):
  l=len(n)
  a=[]
  sums=[]
  maxsum=0
  for i in range(l+1):
    for j in range(i+1,l+1):
      a.append(n[i:j]) 
  # print(a)
  for _ in a:
    sums.append(sum(_))
  for _ in sums:
    maxsum=max(maxsum,_)  

  print(maxsum)
maximumsubarray(n)  
     
