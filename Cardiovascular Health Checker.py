import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
f=pd.read_csv('cardio_train.csv',sep=';')
_var1,height,weight,chlo,gluo,age,gen,hibp,lobp,smo,alco,car=0,0,0,0,0,0,0,0,0,0,0,0

#A function to find BMI for Dataframe
def bmi(r):
    h=f.iloc[r,3]
    w=f.iloc[r,4]
    bmi=w/((h/100)**2)
    '''if bmi<=18.5:
        print('Underweight')
    elif bmi>18.5 and bmi<29.9:
        print('Normal Weight')
    elif bmi>=30:
        print('Obesity')
    else: 
        pass'''
    return(bmi)
#A function to find BMI for given
def bmin(h,w):
    bmi=w/((h/100)**2)
    '''if bmi<=18.5:
        print('Underweight')
    elif bmi>18.5 and bmi<29.9:
        print('Normal Weight')
    elif bmi>=30:
        print('Obesity')
    else: 
        pass'''
    return(bmi)

#print(f)

def inp():
#Getting Input

    age1=int(input('Enter AGE in Years : '))
    age1+=1095
    gender1=int(input('Enter 1 for MALE and 2 for FEMALE : '))
    height1=int(input('Enter Height in cm : '))
    weight1=int(input('Enter weight in kg : '))
    hibp1=int(input('Enter the High Action Pulse (AP) : '))
    lwbp1=int(input('Enter the Low Action Pulse (AP) : '))
    chl1=int(input('Enter Cholesterol 1/2/3 : '))
    glu1=int(input('Enter Glucose 1/2/3 : '))
    smo1=int(input('Do you Smoke? 0/1 : '))
    alco1=int(input('Do you consume Alcohol? 0/1: '))
    car1=int(input('Doing Cardio? 0/1 : '))

# Using numpy  where function can be sort the list by required condition
    
    _a=np.where(f['age']+5<=age1)
    _b=np.where(f['gender']==gender1)
    _c=np.where(f['ap_hi']<=hibp1)
    _d=np.where(f['ap_lo']>=lwbp1)
    _e=np.where(f['cholesterol']<=chl1)
    _f=np.where(f['gluc']==glu1)
    _g=np.where(f['smoke']==smo1)
    _h=np.where(f['alco']==alco1)
    _z=np.where(f['cardio']==car1)

# Converting the Input data into set
     
    seta=set(dict.fromkeys(_a[0]))
    setb=set(dict.fromkeys(_b[0]))
    setc=set(dict.fromkeys(_c[0]))
    setd=set(dict.fromkeys(_d[0]))
    sete=set(dict.fromkeys(_e[0]))
    setf=set(dict.fromkeys(_f[0]))
    setg=set(dict.fromkeys(_g[0]))
    seth=set(dict.fromkeys(_h[0]))
    setz=set(dict.fromkeys(_z[0]))
    set_int=setz.intersection(seth.intersection(setg.intersection(setf.intersection(sete.intersection(setd.intersection(setc.intersection(setb.intersection(seta))))))))
    return(set_int,height1,weight1,chl1,glu1,age1,gender1,hibp1,lwbp1,smo1,alco1,car1)

#Condition when zero occurs

def zero():
    possi=0
    wrg=0
    global _var1,height,weight,chlo,gluo,age,gen,hibp,lobp,smo,alco,car
#BMI
    if bmin(height,weight)>=30:
        possi+=25
    elif bmin(height,weight)<30 and bmin(height,weight)>=25:
         possi+=18
    else:
        pass
#High Action Potential
    if hibp>=135:
        possi+=7
    elif hibp<135 and hibp>=115:
        possi+=5
    else:
        pass
#Low Action Potential
    if lobp<=60 and lobp>45:
        possi+=4
    elif lobp<=45:
        possi+=7
    else:
        pass
#cholestrol
    if chlo==3:
        possi+=18
    elif chlo==2:
        possi+=14
    elif chlo==1:
        possi+=8
    else:
        wrg=1
#Glucose
    if gluo==3:
        possi+=14
    elif gluo==2:
        possi+=8
    elif gluo==1:
        possi+=3
    else:
        wrg=1
#Smoking
    if smo==1:
        possi+=16
    elif smo==0:
        possi+=1
    else:
        wrg=1
#Alcohol
    if alco==1:
        possi+=5
    elif alco==0:
        possi+=1
    else:
        wrg=1

#Age and Gender
    if gen==1:
        if age>=16447:
            possi+=7
        elif age<16447 and age>=10950:
            possi+=3
        elif age<10950 and age>=7320:
            possi+=1
        else:
            pass
    elif gen==2:
        if age>=20289:
            possi+=5
        elif age<16447 and age>=10950:
            possi+=2
        elif age<10950 and age>=7320:
            possi+=1
        else:
            pass
    else:
        wrg=1
#cardio
    if car==1:
        possi-=10
    elif car==0:
        pass
    else:
        wrg=1

    if wrg==1:
        print("\n\nKindly select the Appropriate Option\n\n")
        _var1,height,weight,chlo,gluo,age,gen,hibp,lobp,smo,alco,car=inp()
        return True
    else:
        if possi>=40:
            print("\n This Person may have Cardio Problem!.\n Kindly visit Hospital. \n Don't Smoke and Don't Drink")
        elif possi<40:
            print("\n This Person does not have any thread to Cardio Problem.\n Don't Smoke and Don't Drink")  
        return False

# Declaring Variable
_var1,height,weight,chlo,gluo,age,gen,hibp,lobp,smo,alco,car=inp()

#Decided whether to use Data or Program
if len(_var1)==0:
    #print('Program at Starting')
    flag=True
    while(flag==True):
        flag=zero()
else:
    n_active=0
    n_count=0
    for i in _var1:
        if bmin(height,weight)>=bmi(i):
            #print('BMI executed!!!')
            if chlo==f.iloc[i,7] or gluo==f.iloc[i,8]:
                n_count+=1
                #print(n_count)
                #print('Chlo or Gluo executed!!')
                #print(f.iloc[i,11])
                if f.iloc[i,11]==1:
                    n_active+=1
                    #print(f.iloc[i])
    print('\n Total number of Case similar to Given Data : ',n_count)
    print('\n Total number of Active Case in the Data : ',n_active)
    if n_count==0:
        #print('Program at End')
        zero()
    elif (n_active/n_count)*100>=60:
        #print('Machine Learning')
        print("\n This Person may have Cardio Problem!.\n Kindly visit Hospital. \n Don't Smoke and Don't Drink")
    else:
        #print('Machine Learning')
        print("\n This Person does not have any thread to Cardio Problem.\n Don't Smoke and Don't Drink")

#Plot for reference
f.plot(kind='line',x='ap_hi',y='ap_lo',rot=0)
#f.plot(kind='scatter',x='ap_lo',y='age',rot=0)
plt.show()