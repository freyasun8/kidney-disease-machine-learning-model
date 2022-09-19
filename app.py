 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(age, wc, htn, dm):   
 
    # Pre-processing user input    
    if htn == "no":
        htn = 0
    else:
        htn = 1
 
    if dm == "no":
        dm = 0
    else:
        dm = 1
 
      
    # Making predictions 
    prediction = classifier.predict( 
        [[age, wc, htn, dm]])
     
    if prediction == 0:
        pred = 'Kidney Disease not detected'
    else:
        pred = 'Kidny Disease found'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:cyan;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Kidney Disease Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    htn = st.selectbox('htn',("no","yes"))
    dm = st.selectbox('dm Status',("no","yes")) 
    age = st.number_input("AGE") 
    wc = st.number_input("WC")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(age, wc, htn, dm) 
        st.success('Report Results: {}'.format(result))
        
     
if __name__=='__main__': 
    main()
