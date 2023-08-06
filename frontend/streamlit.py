import streamlit as st
import requests
import json
import os

API_URL = os.getenv('API_URL') 

# Simple title and descriptions
st.title('Medical Cost Calculator')

post_dictionary = { "sex_male": 0,
                    "smoker_yes": 0,
                    "region_northwest": 0,
                    "region_southeast": 0,
                    "region_southwest": 0,
                    "age": 24,
                    "bmi": 24,
                    "children": 0 }


# get available airports from API and save selection to a variable
gender = st.selectbox("Choose your gender:", ['Male','Female'])
if gender == "Male":
    post_dictionary['sex_male'] = 1

smoker = st.radio("Are you a smoker?:", ['Yes','No'])
if gender == "Yes":
    post_dictionary['smoker_yes'] = 1

location = st.selectbox("Which part of the US do you live in?:", ['North West','North East', 'South West', 'South East'])
if location == "North West":
    post_dictionary['region_northwest'] = 1
elif location == "South East":
    post_dictionary['region_southeast'] = 1
elif location == "South West":
    post_dictionary['region_southwest'] = 1

age = st.number_input("What is your age?",min_value=0,max_value=99)
bmi = st.number_input("What is your Boyd Mass Index (BMI)?",min_value=10.0,max_value=50.0)
children = st.number_input("How many children do you have?",min_value=0,max_value=10)
post_dictionary['age'] = age
post_dictionary["bmi"] = bmi
post_dictionary["children"] = children

# get the result from mongodb database when button is trigger
if st.button('GET'):
    prediction = requests.post(API_URL,json.dumps(post_dictionary))
    st.write("Your medical bill is predicted to cost about $" + str(int(json.loads(prediction.text)["cost"])))
