
# coding: utf-8

# In[19]:


proc=[]
alloc=[]
maxm=[]
need=[]
avail=[]
finish=[]
work=[]

n = int(input('Enter the total no of processes: '))
for i in range(n):
    proc.append([])
    proc[i].append(input('Enter process'+str(i+1)+' name: '))
    
for i in range(n):
    alloc.append([])
    alloc[i].append(int(input('Enter allocation for X of '+str(proc[i])+' : ')))
    alloc[i].append(int(input('Enter allocation for Y of '+str(proc[i])+' : ')))
    alloc[i].append(int(input('Enter allocation for Z of '+str(proc[i])+' : ')))

for i in range(n):
    maxm.append([])
    maxm[i].append(int(input('Enter Max allocation for X of '+str(proc[i])+' : ')))
    maxm[i].append(int(input('Enter Max allocation for Y of '+str(proc[i])+' : ')))
    maxm[i].append(int(input('Enter Max allocation for Z of '+str(proc[i])+' : ')))
    
for i in range(3):
    avail.append([])
    avail[i].append(int(input('Enter Available m/m: ')))
    
for i in range(n):
    need.append([])
    for j in range(3):  
        need.append([])
        need[i].append(maxm[i][j] - alloc[i][j])
print ('\n\n\t\tAllocated\t\tMaximum\t\t\tNeed')        
print ('ProcessName\tX\tY\tZ\tX\tY\tZ\tX\tY\tZ')
for i in range(n):
    print (str(proc[i][0])+'\t\t'+str(alloc[i][0])+'\t'+str(alloc[i][1])+'\t'+str(alloc[i][2])+'\t'+str(maxm[i][0])+'\t'+str(maxm[i][1])+'\t'+str(maxm[i][2])+'\t'+str(need[i][0])+'\t'+str(need[i][1])+'\t'+str(need[i][2]))
    
print ('\tAvailable')
print ('X = '+str(avail[0]))
print ('Y = '+str(avail[1]))
print ('Z = '+str(avail[2]))

for i in range(3):
    work.append(avail[i][0])
    
for i in range(n):
    finish.append(0)
flag=0
for i in range(n):
    for j in range(3):
        if (finish[i]==0 and need[i][j]<work[j]):
            work[j]=work[j]+alloc[i][j]
            finish[i]=1
            
        else:
            flag=flag+1
    if flag==5:
        break

if 0 in finish:
    print('\n\nUNSAFE')
else:
    print('\n\nSAFE')
    
    


# ## 
