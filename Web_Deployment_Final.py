import pickle
import streamlit as st

# Load Model
stock_model = pickle.load(open('Stock_Data.sav', 'rb'))

def predict_ltp(VWAP, Delta):
    ltp_prediction = stock_model.predict([[VWAP, Delta]])
    return ltp_prediction[0]

def main():
    st.title('Stock Prediction')

    html_temp = """
    <div style="background-color:tomato;padding:10px;">
    <h2 style="color:white;text-align:center;">Stock Prediction ML Model</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    VWAP = st.text_input("VWAP", "Type Here")
    Delta = st.text_input("Delta", "Type Here")

    result = ""

    if st.button("Predict"):
        try:
            VWAP = float(VWAP)
            Delta = float(Delta)
            result = predict_ltp(VWAP, Delta)
            st.success(f"Predicted LTP: {result}")
        except ValueError:
            st.error("Please enter valid numeric values for VWAP and Delta")

if __name__ == '__main__':
    main()