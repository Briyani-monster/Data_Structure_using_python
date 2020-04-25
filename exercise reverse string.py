def reverse(stri):
  if len(str(stri))<2 or not type(stri)==str:
    return 'hmm something is wrong here'
  back=[]
  li=list(stri)
  i=len(stri)
  while not i==0:
    back.append(li[i-1])
    i-=1
  return "".join(back)
print(reverse('hello i am kishan'))
print(reverse(1234))
print(reverse(''))    
