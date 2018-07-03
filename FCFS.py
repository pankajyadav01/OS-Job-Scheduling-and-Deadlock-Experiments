
# coding: utf-8

# In[5]:


queue = []
total_time = 0
total_tattime=0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    queue.append([])
    queue[i].append(input('Enter process name: '))
    queue[i].append(int(input('Enter process arrival time: ')))
    queue[i].append(int(input('Enter process burst time: ')))   
queue.sort(key = lambda queue:queue[1])
for i in range(n):
    queue.append([])  
    total_time += queue[i][2]
    queue[i].append(total_time)
    queue[i].append(total_time-queue[i][1])
    total_tattime += queue[i][4]

print ('ProcessName\tArrivalTime\tBurstTime\tWaitingTime\tTurnAroundTime')
for i in range(n):
    print (str(queue[i][0])+'\t\t'+str(queue[i][1])+'\t\t'+str(queue[i][2])+'\t\t'+str(queue[i][3])+'\t\t'+str(queue[i][4]))


# In[6]:


print ("Total waiting time = "+str(total_time))


# In[7]:


print ("Average waiting time = "+str(total_time/n))


# In[8]:


print ("Total TurnAround time = "+str(total_tattime))
print ("Average TurnAround time = "+str(total_tattime/n))

