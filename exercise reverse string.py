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

#using build in function  
def reverse1(stri):
  if len(str(stri))<2 or not type(stri)==str:
    return 'hmm something is wrong here'
  li=list(stri)
  li.reverse()
  return "".join(li)  

print(reverse('hello i am kishan'))
print(reverse(1234))
print(reverse('hello my name is andrei'))  
print("second function")
print(reverse1('hello i am kishan'))
print(reverse1(1234))
print(reverse1('hello my name is andrei'))  


