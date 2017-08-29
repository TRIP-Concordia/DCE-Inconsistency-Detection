# Ali's first program!
# Zachary Patterson: 18 August 2015


import csv
import datetime
# Can also import reader like this...
#from csv import reader
#import logging

maxalt=7
maxtask=6

print "Reading in a file"

#infilepath = 'test.csv'
#outfilepath = 'test_out.csv'

# This is a list into which we will put the data we read in
dataset = []
standard= []
mutual = []

with open('C:\\Users\\ali\\Dropbox\\Paper\\Journal\\Inconcistencies in Choice Behaviour\\Analysis\\Ricardo\\Python\\Input.csv', 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		dataset.append(line)
#making standard dataset, in which all attributes has positive coefficients

standard.append(['id','task'])
standard.append(['n', 'n'])
for i in range(1,len(dataset[0])-2):
    standard[0].append('att'+str(i))
    standard[1].append(dataset[1][i+1])
standard[0].append('Choice')
standard[1].append('+')

for i in range(2,len(dataset)):
    standard.append([0,0])
    standard[i][0]=dataset[i][0]
    standard[i][1]=dataset[i][1]
    for j in range(2,len(dataset[0])):
        if dataset[1][j]=="-":
            standard[i].append(-float(dataset[i][j]))
        else:
            standard[i].append(float(dataset[i][j]))
 
            
with open('C:\\Users\\ali\\Dropbox\\Paper\\Journal\\Inconcistencies in Choice Behaviour\\Analysis\\Ricardo\\Python\\standard.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(standard)
    
print('standard',datetime.datetime.now())    

mutual.append(['id','task'])
for i in range(1,len(dataset[0])-2):
    mutual[0].append('att'+str(i))
mutual[0].append('Choice') 
mutual[0].insert(2,'case')
mutual[0].append('eff_att')
mutual[0].append('inconsistent')
mutual[0].append('counter')
mutual[0].append('sum_task')
mutual[0].append('sum_id')	


c=0	
for i in range(2,len(standard)):
    if standard[i][standard[0].index('task')]!=standard[i-1][standard[0].index('task')]:
        for j in range(maxalt):
            if standard[i][standard[0].index('task')]==standard[i+j][standard[0].index('task')]:
                for k in range(maxalt):
                    if standard[i][standard[0].index('task')]==standard[i+k][standard[0].index('task')]:

                        
                        if float(standard[i+j][standard[0].index('Choice')])+float(standard[i+k][standard[0].index('Choice')])==1 :
                            #if float(standard[i+j][standard[0].index('av_alt')])+float(standard[i+k][standard[0].index('av_alt')])==2 :
                                c +=1
                                id = int(standard[i][standard[0].index('id')])
                                task = int(standard[i][standard[0].index('task')])
                                case= ", ".join([str(j+1), str(k+1)])
                                mutual.append([id,task,case])
                                
                                for l in range(1,len(standard[0])-2):
                                    if float(standard[i+j][standard[0].index('att'+str(l))])!=999:
                                        v=float(standard[i+j][standard[0].index('att'+str(l))])-float(standard[i+k][standard[0].index('att'+str(l))])
                                        mutual[c].append(v)
                                    else:
                                        v=999
                                        mutual[c].append(v)

                                Choice = float(standard[i+j][standard[0].index('Choice')])-float(standard[i+k][standard[0].index('Choice')])
                                mutual[c].append(Choice)
                                mutual[c].append(0)
                                mutual[c].append(0)
                                mutual[c].append(0)
                                mutual[c].append(0)
                                mutual[c].append(0)


print('mutual',datetime.datetime.now())
    
Dominance=len(standard[0])-3
Equality=standard[1].count('+')+standard[1].count('-')-1

 
for i in range(1,len(mutual)):
    if mutual[i][mutual[0].index('id')]!=mutual[i-1][mutual[0].index('id')]:
        Omitted=mutual[i].count(999)
        for j in range(0,2*(maxalt-1)*maxtask):
            if (i+j) < len(mutual):
                if mutual[i][mutual[0].index('id')]==mutual[i+j][mutual[0].index('id')]:
                    counter=0
                    effective=""
                    inconsistent=""
                    for k in range(0,2*(maxalt-1)*maxtask):
                        if (i+k) < len(mutual):
                            if mutual[i][mutual[0].index('id')]==mutual[i+k][mutual[0].index('id')]:
                                b=0
                                c=0
                                #effective_att dummy
                                d=0
                                #effective_att non-dummy
                                e=0   
                                                             
                                if mutual[i+j][mutual[0].index('Choice')]>mutual[i+k][mutual[0].index('Choice')]:
                                                                   
                                    for l in range(1,len(standard[0])-2):
                                        if mutual[i][mutual[0].index('att'+str(l))]!=999:
                                            if standard[1][standard[0].index('att'+str(l))]=='n':
                                                if mutual[i+j][mutual[0].index('att'+str(l))]==mutual[i+k][mutual[0].index('att'+str(l))]:
                                                    b +=1
                                                else:
                                                    d +=1
                                                    if d==1:
                                                        effective_att1='att'+str(l)
                                                    elif d==2:
                                                        effective_att2='att'+str(l)   
                                               
                                            else:
                                                if mutual[i+j][mutual[0].index('att'+str(l))]<=mutual[i+k][mutual[0].index('att'+str(l))]:
                                                    b +=1
                                                    if mutual[i+j][mutual[0].index('att'+str(l))]==mutual[i+k][mutual[0].index('att'+str(l))]:
                                                        c +=1
                                                else:
                                                    e +=1
                                                    if e==1:
                                                        efective_att='att'+str(l)
                                                                                                        
                                                               
        
                                elif mutual[i+j][mutual[0].index('Choice')]<mutual[i+k][mutual[0].index('Choice')]:

                                    for l in range(1,len(standard[0])-2):
                                        if mutual[i][mutual[0].index('att'+str(l))]!=999:
                                            if standard[1][standard[0].index('att'+str(l))]=='n':
                                                if mutual[i+j][mutual[0].index('att'+str(l))]==mutual[i+k][mutual[0].index('att'+str(l))]:
                                                    b +=1
                                                else:
                                                    d +=1
                                                    if d==1:
                                                        effective_att1='att'+str(l)
                                                    elif d==2:
                                                        effective_att2='att'+str(l)                                                          
                                                    
                                            else:
                                                if mutual[i+j][mutual[0].index('att'+str(l))]>=mutual[i+k][mutual[0].index('att'+str(l))]:
                                                    b +=1
                                                    if mutual[i+j][mutual[0].index('att'+str(l))]==mutual[i+k][mutual[0].index('att'+str(l))]:
                                                        c +=1
                                                else:
                                                    e +=1
                                                    if e==1:
                                                        effective_att='att'+str(l)
                                                                                                                                                           
                                if b==Dominance-Omitted:
                                    if c<Equality-Omitted:
                                        new_case=str(mutual[i+k][mutual[0].index('task')]) + '; ' + mutual[i+k][mutual[0].index('case')]
                                        inconsistent=inconsistent+'('+new_case+")"
                                        counter +=1
                                elif d==2:
                                    if e==0:
                                        effect_att=effective_att1 + ',' + effective_att2
                                        new_case=str(mutual[i+k][mutual[0].index('task')]) + '; ' + mutual[i+k][mutual[0].index('case')]+ ';' + effect_att
                                        effective=effective+'('+new_case+")"                                        
                                        
                                elif d==0:
                                    if e==1:
                                        effect_att=effective_att
                                        new_case=str(mutual[i+k][mutual[0].index('task')]) + '; ' + mutual[i+k][mutual[0].index('case')]+ ';' + effect_att
                                        effective=effective+'('+new_case+")"
                                                                        
                                                                                                                
                            else:
                                break 
                    
                    mutual[i+j][mutual[0].index('eff_att')]=effective
                    mutual[i+j][mutual[0].index('inconsistent')]=inconsistent
                    mutual[i+j][mutual[0].index('counter')]=counter                                                                                              
                                        
                else:
                    break

        sum_task=0
        sum_id=0
        k=0
        for j in range(0,2*(maxalt-1)*maxtask+1):
            if (i+j) < len(mutual):
                if mutual[i][mutual[0].index('id')]==mutual[i+j][mutual[0].index('id')]:
                    sum_id=sum_id+mutual[i+j][mutual[0].index('counter')]
                    if mutual[i+j][mutual[0].index('task')]==mutual[i+j-1][mutual[0].index('task')]:
                        sum_task=sum_task+mutual[i+j][mutual[0].index('counter')]
                    else:
                        mutual[i+k][mutual[0].index('sum_task')]=sum_task/2
                        k=j
                        sum_task=mutual[i+j][mutual[0].index('counter')]
                else:
                    mutual[i+k][mutual[0].index('sum_task')]=sum_task/2
                    break
            elif (i+j)==len(mutual):
                mutual[i+k][mutual[0].index('sum_task')]=sum_task/2                                    
        mutual[i][mutual[0].index('sum_id')]=sum_id/2

 
with open('C:\\Users\\ali\\Dropbox\\Paper\\Journal\\Inconcistencies in Choice Behaviour\\Analysis\\Ricardo\\Python\\mutual.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(mutual)                                     
 
print('inconsistency',datetime.datetime.now())
                                                                                                                                                                                                                        
sum_task=[]
sum_id=[]

sum_task.append(['id','task','sum_task'])
sum_id.append(['id','task','sum_id'])
for i in range(1,len(mutual)):
    if mutual[i][mutual[0].index('task')]!=mutual[i-1][mutual[0].index('task')]:
        id = int(mutual[i][mutual[0].index('id')])
        task = int(mutual[i][mutual[0].index('task')])
        sum_task1=int(mutual[i][mutual[0].index('sum_task')])
        sum_task.append([id,task,sum_task1])

        if mutual[i][mutual[0].index('id')]!=mutual[i-1][mutual[0].index('id')]:
            sum_id1=int(mutual[i][mutual[0].index('sum_id')])
            sum_id.append([id,task,sum_id1])
        

print "Write out our data using csv writer"

with open('C:\\Users\\ali\\Dropbox\\Paper\\Journal\\Inconcistencies in Choice Behaviour\\Analysis\\Ricardo\\Python\\sum_task.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(sum_task)
    
with open('C:\\Users\\ali\\Dropbox\\Paper\\Journal\\Inconcistencies in Choice Behaviour\\Analysis\\Ricardo\\Python\\sum_id.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(sum_id)

#test_dict = {}
