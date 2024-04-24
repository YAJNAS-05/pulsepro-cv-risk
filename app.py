import streamlit as st
import pandas as pd
import numpy as np
f=pd.read_csv('cardio_train.csv',sep=';')
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

#A function to find BMI for Dataframe
def bmi(r):
    h=f.iloc[r,3]
    w=f.iloc[r,4]
    bmi=w/((h/100)**2)
    return(bmi)
#A function to find BMI for given
def bmin(h,w):
    bmi=w/((h/100)**2)
    return(bmi)

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

def inp(age1,gender1,height1,weight1,hibp1,lwbp1,chl1,glu1,smo1,alco1,car1
):
# age1,gender1,height1,weight1,hibp1,lwbp1,chl1,glu1,smo1,alco1,car1

# Using numpy  where function can be sort the list by required condition
    
    _a=np.where(f['age']+1095<=age1)
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


# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome to Pulse Pro")
    st.subheader("Cardio Vascular Analysis ")
    st.write("How's your heart doing ?")
    st.write("Please enter your details below to receive a personalized cardiovascular analysis. \n Your health is our priority, let's get started!")
    age1=st.number_input('Enter AGE in Years : ',min_value=0)
    age1*=365
    gender1=st.number_input('Enter 1 for MALE and 2 for FEMALE : ',min_value=0)
    height1=st.number_input('Enter Height in cm : ',min_value=0)
    weight1=st.number_input('Enter weight in kg : ',min_value=0)
    hibp1=st.number_input('Enter the High Action Pulse (AP) : ',min_value=0)
    lwbp1=st.number_input('Enter the Low Action Pulse (AP) : ',min_value=0)
    chl1=st.number_input('Enter Cholesterol 1/2/3 : ',min_value=0)
    glu1=st.number_input('Enter Glucose 1/2/3 : ',min_value=0)
    smo1=st.number_input('Do you Smoke? 0/1 : ',min_value=0)
    alco1=st.number_input('Do you consume Alcohol? 0/1: ',min_value=0)
    car1=st.number_input('Doing Cardio? 0/1 : ',min_value=0)
count=0
if st.button("Predict"):
    _var1,height,weight,chlo,gluo,age,gen,hibp,lobp,smo,alco,car=inp(age1,gender1,height1,weight1,hibp1,lwbp1,chl1,glu1,smo1,alco1,car1)
    if len(_var1)==0:
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
        st.write(' Total number of Case similar to Given Data : ',n_count)
        st.write(' Total number of Active Case in the Data : ',n_active)
        if n_count==0:
            #print('Program at End')
            zero()
        elif (n_active/n_count)*100>=60:
            #print('Machine Learning')
            #st.write(" This Person may have Cardio Problem!.\n Kindly visit Hospital. \n Don't Smoke and Don't Drink")
            count=-1
        else:
            #print('Machine Learning')
            #st.write("This Person does not have any thread to Cardio Problem.\n Don't Smoke and Don't Drink")
            count=1
with st.container():
    if count==1:
        st.write("This Person does not have any thread to Cardio Problem.\n Don't Smoke and Don't Drink")
    elif count==-1:
        st.write(" This Person may have Cardio Problem!.\n Kindly visit Hospital. \n Don't Smoke and Don't Drink")
