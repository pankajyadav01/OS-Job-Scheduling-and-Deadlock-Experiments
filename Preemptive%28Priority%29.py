
# coding: utf-8

# In[1]:


l1=[['p1',9,5],['p2',8,1],['p3',7,3],['p4',2,5],['p5',3,2]]
burst1=[]
for i in range(0,5):
    burst1.append(l1[i][1])
l1.sort(key=lambda x:x[1])
print(l1)
burst=[]
priority=[]
process=[]
completion=[]
process_run=[]
turn_around=[]
wait=[]
for i in range(0,5):
    process.append(l1[i][0])
    burst.append(l1[i][1])
    priority.append(l1[i][2])
print(process,burst,priority)
process1=process[:]
burst[0]=burst[0]-1
completion.append(1)
process_run.append(process[0])

for i in range(0,5):
    for j in range(1,5):
        if priority[j-1]>priority[j]:
            temp=priority[j-1]
            priority[j-1]=priority[j]
            priority[j]=temp
            temp2=burst[j-1]
            burst[j-1]=burst[j]
            burst[j]=temp2
            temp3=process[j-1]
            process[j-1]=process[j]
            process[j]=temp3
print(process)
print(priority)
print("Modified burst")
print(burst)
print(burst1)
for i in range(1,len(priority)+1):
    a=completion[i-1]
    completion.append(a+burst[i-1])
    process_run.append(process[i-1])
print("Process running in the sequence")
print(process_run)
print("Completion time")
print(completion)
index=100
for i in range(0,len(process)):
    for j in range(0,len(process_run)):
        if process[i]==process_run[j]:
            index=j
    turn_around.append(completion[index])
print(process)
print(turn_around)
new=[]
e=0
for i in range(0,5):
    new.append([])
    for j in range(0,1):
        new[i].append(process[e])
        new[i].append(turn_around[e])
        e=e+1
print(new)
new.sort(key=lambda x:x[0])
print(new)
turn_around1=[]
for i in range(0,5):
    turn_around1.append(new[i][1])
print("Turn around1 is")
print(turn_around1)
sum1=0
for i in range(0,5):
    a=turn_around1[i]-burst1[i]
    sum1=sum1+a
    wait.append(a)
print(wait)
print("Average wait time is",sum1/5)

