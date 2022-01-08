import random

n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist = ["Jadeja","Ashwin","Rahena"]
myList2={"Jadeja","Ashwin","Raehna"}
mydict={'Andhra Pradesh' :'andhraa','Bihar':'Patna','Hyderabad':'Telagana'}
entry_list = list(mydict.items())
random.shuffle(entry_list)
ans=dict(zip(mydict,entry_list))#dictionary
print(ans)
random_entry = random.choice(entry_list)
print(random_entry)
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)