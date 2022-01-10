import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import *
from keras.layers import *
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional

from PIL import Image
import pandas as pd

# interface
st.title('Vietnamese fake news detector')
image = Image.open('./data/output.png')
st.image(image)
form = st.form(key='my_form')
text_input = form.text_input('Insert a piece of news here')
option = form.selectbox('Choose your model', ('Logistic Regression', 'Long short-term memory'))
submit_button = form.form_submit_button('Predict')

# function
def create_model():
    # Sequential Model  
    model = Sequential()
    # embeddidng layer
    model.add(Embedding(8486, output_dim = 128))
    # Bi-Directional RNN and LSTM
    model.add(Bidirectional(LSTM(128)))
    # # Dense layers
    model.add(Dense(128, activation = 'relu'))
    model.add(Dense(1,activation= 'sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
    return model

def pred(x):
    if x > 0.5:
        return 1
    else:
        return 0

def main():
    X_df = pd.read_csv('./data/X_df.csv')
    class_name = ["Fake news", "Real news"]

    if option == 'Logistic Regression':
        # load model
        pickle_in = open('./model/lr_model.pkl', 'rb') 
        lr = pickle.load(pickle_in)
        tfidf = TfidfVectorizer(ngram_range= (1,3), lowercase= True, max_features= 5000)
        X_transformed = tfidf.fit_transform(X_df['clean_joined'])
        text_transformed = tfidf.transform([text_input])
        result = lr.predict(text_transformed)
        class_id = np.argmax(result)
        st.write('Result: ', class_name[class_id])    

    if option == 'Long short-term memory':
        # create model
        model = create_model()
        # load model
        model.load_weights('./model/lstm_model/')
        tokenizer = Tokenizer(num_words = 8486)
        tokenizer.fit_on_texts(X_df['clean_joined'])
        test = tokenizer.texts_to_sequences([text_input])
        result = pred(model.predict(test)[0][0])
        st.write('Result: ', class_name[result])    

if __name__ == "__main__":
    main()
