import streamlit as st
import pickle as pk
import numpy as np         
    
model = pk.load(open("diabetesPrediction.pkl","rb"))
sc = pk.load(open("scaler.pkl","rb"))

# adding style to the website 
st.markdown("""
<style>
            
.stSelectbox:first-of-type > div[data-baseweb="select"] > div {
    font-weight:bold;
}

input[class]
{
    font-weight:bold;
}
                
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 23px;
    margin-left:-30%;
}
            
.st-emotion-cache-1vbkxwb p {
    padding: 0px 5px 2px 5px;
    transform:scale(1.4);
            
    
} 
.st-emotion-cache-keje6w {
    width: calc(30% - 1rem);
    flex: 1 2 calc(40% - 1rem);
    /* padding-left: 50px; */
    margin-left: 41%;
}
            
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ffffff;
}
div.stButton > button:focus:not(:active) {
    color:#ffffff;
    background-color:#0099ff;  
}
div.stButton > button
{
    transform:scale(1.1);
    padding:7px 10px;
    margin:5px 0px 7px 14px;
}
</style>""", unsafe_allow_html=True)


feet_meter = 30.48
gender_map = {'Male':0 , 'Female':1 , 'Other':2}
smoking_map = {'never': 0,'current': 1, 'former': 2, 'ever': 3, 'not current': 4} 
Bintoint_map = {'Yes':1 , 'No':0}

st.markdown("<h1 style='text-align : center;margin-bottom:5px;margin-left:-15px; '>Diabetes Prediction</h1>",unsafe_allow_html=True)

gender = st.selectbox("Gender",label_visibility="collapsed",options=['Male','Female','Other'],index=None , placeholder="Gender")
age = st.number_input("Age",label_visibility="collapsed",placeholder="Age" , value=None)   
c1,c2= st.columns(2)
with c1:
    hypertension = st.radio("High Tension",["Yes","No"])
ch1,ch2= st.columns(2)
with ch1:
    heartattack = st.radio("Heart Attack symptoms",options = ["Yes","No"])
smoking = st.selectbox("smoking",label_visibility="collapsed",options=["never","current","former","ever" ,"not current"],index=None , placeholder="Smoking ")
weight = st.number_input("weight",label_visibility="collapsed",value = None ,placeholder="Weight(in kg)")
height = st.number_input("height" , label_visibility="collapsed",value=None , placeholder="Height(in feet)")

if height==None:
    height=1    
if weight==None:
    weight=0

height = height * feet_meter
bmi = weight / (height * height ) *(10000)
bmi = str(bmi)[:5]
val = st.subheader("‎ ‎ ‎ BMI = " +str(bmi))   

himoglobina1c = st.number_input("HbA1c_level" , label_visibility="collapsed" ,value=None, placeholder="Himoglobin A1C level")
bloodglucose = st.number_input("Blood Glucose Level" , label_visibility="collapsed" , value=None , placeholder="Blood Glucose Level")


col1, col2, col3,c4,c5 = st.columns(5)
with col3:
    diabetespredicition = st.button("Predict" )

def giveResult(res):
    st.markdown("<style>.container{;}</style>",unsafe_allow_html=True)
    if res==0:
        st.markdown('<h1 style="text-align:center">You don\'t have diabetes</h1><img style = "display:block ; margin:0 auto" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3Axem1kc2kwZ3dqNHZqcWhsb3ZyYXNlZ2ExOWk0MHR4Y3hzNzZsNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SnLkU2XG1z5io/giphy.gif"/>', unsafe_allow_html=True)
    else:
        st.markdown('<h1 style="text-align:center">You have diabetes</h1><img style = "display:block ; margin:0 auto" src="https://media.giphy.com/media/gfsQffBnuc6e096brx/giphy.gif"/>', unsafe_allow_html=True)
def checkallvalues():
    if gender==None or smoking==None or hypertension==None or heartattack==None or bmi==None or himoglobina1c==None or bloodglucose==None:
        st.markdown("<h1 style='text-align:center;color:red' >Enter all details</h1>",unsafe_allow_html=True)
        return False
    return True

def PredictDiabetes():
    if checkallvalues():
        gender_convert = gender_map[gender]
        smoking_convert = smoking_map[smoking] 
        hypertension_convert = Bintoint_map[hypertension]
        heartattack_convert = Bintoint_map[heartattack]
        
        # st.write(Bintoint_map[hypertension])
        newdata = [gender_convert,age,hypertension_convert,heartattack_convert,smoking_convert,bmi,himoglobina1c,bloodglucose]
        reshaped_data = np.array(newdata).reshape(1,-1 )
        scaled_data = sc.transform(reshaped_data)
        res = model.predict(scaled_data)[0]
        
        giveResult(res)


if diabetespredicition:
    PredictDiabetes()
