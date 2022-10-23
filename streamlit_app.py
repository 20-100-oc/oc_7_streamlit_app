# Front end app to interact with sentiment prediction API.
# To use this, initialize the API first.
# Then type in cmd: streamlit run <name_of_this_file>
#
# Exemple:
# streamlit run scripts/app.py


import streamlit as st
import requests



def main():
    #url = 'http://127.0.0.1:8000/'    # local url
    url = 'https://api-oc-7.azurewebsites.net/'
    
    st.title('Sentiment analysis')
    tweet = st.text_input(label='Insert tweet here', max_chars=280)

    predict_btn = st.button('Predict')
    if predict_btn:
        try:
            keys = {'tweet': tweet}
            raw_res = requests.get(url, params=keys)
            res = raw_res.json()

            st.write('Tweet:', res['tweet'])
            st.write('Sentiment:', res['sentiment'])
            st.write('Probability:', res['probability'])

        except Exception as e:
            st.write(raw_res)
            st.write('Raw json returned by api:')
            st.write(raw_res.text)
            raise e



if __name__ == '__main__':
    main()
