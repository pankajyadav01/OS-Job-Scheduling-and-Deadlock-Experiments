
# coding: utf-8

# In[8]:


queue = []
total_time = 0
total_tattime=0
total_wtime=0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    queue.append([])
    queue[i].append(input('Enter process name: '))
    queue[i].append(int(input('Enter process Priority: ')))
    queue[i].append(int(input('Enter process burst time: ')))   
queue.sort(key = lambda queue:queue[1])
for i in range(n):
    queue.append([])  
    total_time += queue[i][2]
    queue[i].append(total_time)
    queue[i].append(total_time-0)
    total_tattime += queue[i][4]
    queue[i].append(total_time-queue[i][2])
    total_wtime += queue[i][5]

print ('ProcessName\tPriority\tBurstTime\tCompletionTime\tTurnAroundTime\tTurnWaitingTime')
for i in range(n):
    
    print (str(queue[i][0])+'\t\t'+str(queue[i][1])+'\t\t'+str(queue[i][2])+'\t\t'+str(queue[i][3])+'\t\t'+str(queue[i][4])+'\t\t'+str(queue[i][5]))


# In[9]:


print ("Total TurnAround time = "+str(total_tattime))
print ("Average TurnAround time = "+str(total_tattime/n))


# In[10]:


print ("Total Waiting time = "+str(total_wtime))
print ("Average waiting time = "+str(total_wtime/n))

