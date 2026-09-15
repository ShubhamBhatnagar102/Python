import pandas as pd 
import streamlit as st
from google import genai
if "chats" not in st.session_state:
    st.session_state.chats=[]
#creating a api function
def send_prompt(query,file_uploaded=None):
    client = genai.Client(api_key="")
    query=f'''please reply according to query and from file's context(csv_file),if present.
                    {query}
                    file={file_uploaded}
            '''
    interaction= client.interactions.create(
        model='gemini-3.8-flash',
        input=query
    )
    return interaction
st.title('the chat app')
cc= st.container(height=400)

#for displaying the chats in chatbox
def chat_display():
    for chat in st.session_state.chats:
        if chat['user']=='Shubham':
            with cc.chat_message(chat['user']):
                st.write(chat['message'])
        elif chat['user']=='gemini':
            with cc.chat_message(chat['user'],avatar='./gemini_logo.webp'):
                st.write(chat['message'])
chat_display()

if write_prompt:=cc.chat_input('Chat here',accept_file=True,file_type=[".csv"]):
    st.session_state.chats.append({'user':'Shubham','message':write_prompt.text})
    file_upload=None
    if write_prompt.files:
        file_upload=pd.read_csv(write_prompt.files[0])
        file_upload=file_upload.dropna()
        file_upload=file_upload.sample(n=500 ,random_state=42 )
        file_upload=file_upload.to_string()
    response=send_prompt(write_prompt.text,file_upload)
    st.session_state.chats.append({'user':'gemini','message':response.output_text})
    chat_display()
    st.rerun()


        
