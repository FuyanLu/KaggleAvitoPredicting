# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

dkj
"""
import numpy as np
import json as js
import re

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
          mediate_json=json.loads(salaries_json)
          mediate_json[name]=salary
          salaries_json=json.dumps(mediate_json)
          print(salaries_json)
          return salaries_json
 



# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])

import csv
import ast
from datetime import  datetime

# The vec is two one hot, the first three elements make one of one hots
# indicating, searchPara is belong to Para, search para is equal and 
# searchPara include parameters or they are not fully overlaped. 
# And the back two elements make another one hot, indicating whether or not
# the existing keys of SearchPara and Para are matched with each other
    

def paraToVec(searchPara,para):
    vec=[0]*6
    if len(searchPara)==0:
        if len(para)==0:
            return vec
        vec[0]=1
        return vec
    if len(para)==0:
        vec[2]=1
        return vec
    sinclup=True
    pinclus=True
    for keys in searchPara:
        if not keys in para:
            pinclus=False
            break
    for keyp in para:
        if not keyp in searchPara:
            sinclup=False
    if sinclup and pinclus:
        vec[1]=1
    elif not sinclup and pinclus:
        vec[0]=1
    elif sinclup and not pinclus:
        vec[2]=1
    else:
        vec[3]=1
    match=True
    for keys in searchPara:
        if keys in para:
            if not searchPara[keys]==para[keys]:
                match=False
                break
    if match:
        vec[4]=1
    else:
        vec[5]=1
    return vec

# The history click is regularized by the mean and standard deviation
# of the extended files data
def hisclickToVec(hisclickstr):
    if hisclickstr=='':
        return [0.0]
    hisclick=float(hisclickstr)
    mean=0.010101
    standdev=0.01425
    hisclickvec=[(hisclick-mean)/standdev]
    return hisclickvec

#By now we use parent category as the predictor
#We may further increase our model by adopting subcategory
# The method by now is one hot vector, it may be improved by
# vtreat method in R. 
    
def categoryToVec(categorystr):
    category=int(categorystr if not categorystr=='' else '1')
    #Parent category has 12 in extended data, the last element
    #denote the new category in larger data set.
    categoryvec=[0]*13
    if category>12:
        categoryvec[12]=1
    else:
        categoryvec[category-1]=1
    return categoryvec
    
# Search location levels, 1-3 into one hot vector
    
def searchlclvToVec(searchlclvstr):
    vec=[0]*3
    vec[int(searchlclvstr)-1]=1
    return vec


# Transform time information into two one hot vec
# One is for week with 1 times 7 one hot vector
# Another is for hours, which is backed into 12 slot
# with each slot is 2 hours. It is 1 times 12 one hot vect  
def timeToVec(timestr):    
    timestr=timestr.replace(".0","") 
    dateTime=datetime.strptime(timestr,'%Y-%m-%d %H:%M:%S')
    vecweek=[0]*7
    vechour=[0]*12
    vecweek[dateTime.weekday()]=1
    vechour[int(dateTime.hour/2)]=1
    print(dateTime.weekday())
    print(vecweek)
    print(dateTime.hour)
    print(vechour)
    a=vecweek+vechour
    print(a)
    return vecweek+vechour


# transform position information into 1 times 2 vec
# The first denote whether or not it is a contex ad
# the second denote it is at position 1 or position 7
def positionToVec(position):
    posivec=[0,0]
    if position=='1':
        posivec[0]=1
        posivec[1]=0
    elif position=='7':
        posivec[0]=1
        posivec[1]=1
    else:
        posivec[0]=0
        posivec[0]=0
    return posivec


# Define the function to transform row to a vector
def rowToVec(row):
    vec=[]
    if row[9]=='':
        searchPara={}
    else:urn vec

    
    
with open('C:\\Users\\Fuyan\\Desktop\\avito-context-ad-clicks\\extended.csv', newline='') as f:
    print("It is fine now")
    
    reader = csv.reader(f)
    # Get header out of cvs file
    header=reader.__next__()
    
    data=[]
        a=re.sub(':{.*?},',":'empty',",row[9])
        searchPara=ast.literal_eval(a)
    if len(row[16])>=1:
        para=ast.literal_eval(row[16])
    else:
        para={}            
    categoryVec=categoryToVec(row[33])
    print("category is :"+row[33])
    searchlclvVec=searchlclvToVec(row[20])
    print("search local level is :"+row[20])
    hisclickVec=hisclickToVec(row[4])
    paraVec=paraToVec(searchPara,para)    
    timeVec=timeToVec(row[8])
    positionVec=positionToVec(row[2])
    isClick=[int(row[5])]
    vec=hisclickVec+paraVec+timeVec+categoryVec+searchlclvVec+positionVec+isClick
    ret
    # the reader.next will jump the first row in same search ID
    # We use lineRestore to restore it
    lineRestore=None
    i=0
    for row in reader:
        if row[0] in ['5522','6609','18227','6608']:
            continue  
        a=row[0]
        rowl=[]
        if not lineRestore==None:
            rowl.append(lineRestore)
        
        # collect all same searchID term together
        # We want to compare the ads in same search 
        # the main data we want to use is the comparation of prices
        # the reader.next will jump the first row in same search ID
        # We use b to restore it
        while row[0]==a:
            rowl.append(row)
            row=reader.__next__()
            lineRestore=row
        if row[0]=='19801':
            break
        numberOfItem=len(rowl)
        mean=0
        MAX=0
        MIN=float(rowl[0][17] if not rowl[0][17]=='' else '0')
        print("the search ID is"+rowl[0][0])
        print(numberOfItem)
        for j in range(numberOfItem):
            price=float(rowl[j][17] if not rowl[j][17]=='' else '0')
            print("price is: %f"%price)
            mean+=price
            if MAX>price:
                MAX=price
            if MIN<price:
                MIN=price
        mean=mean/numberOfItem        
        for ad in rowl:
            if ad[3]=='3':
                price=(float(ad[17] if not ad[17]=='' else '0')-mean)/(MAX-MIN) if not MAX-MIN==0 else 0.0
                print("price is: %f"%price)
                # put the price in the first element of the row vector
                b=[price]+rowToVec(ad)
                print(b)
                print("the total vector length is %d"%len(b))
                data.append(b)
    f.close()
    newtext=open("C:\\Users\\Fuyan\\Desktop\\avito-context-ad-clicks\\newdata.text","wb")
    print(len(data))
    arraydata=np.array(data,dtype=np.dtype(float))
    np.savetxt(newtext,arraydata,fmt='%.4f\t'*2+'%d\t'*43+'%d',delimiter='\t',newline='\r\n')
    newtext.close()    

