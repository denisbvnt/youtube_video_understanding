import streamlit as st
from tasks import get_video_info, interpret_video
from langchain_core.messages import AIMessage, HumanMessage


st.set_page_config(page_title='YouTube video consultant  ▶️', page_icon='▶️')
st.markdown(
    """
    <style>
    label {
        color: white !important;
        font-weight: bold;
    }
    .stApp {
        background-color: #f2f2f2;
    }
    .stSidebar {
        background-color: #ff0033;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('YouTube video consultant ▶️')
st.divider()

language = 'pt'
translation = None
model_options = ['OLlama', 'HuggingFace', 'OpenAI']

if 'model_name' not in st.session_state:
    st.session_state.model_name = model_options[0]

model_name = st.sidebar.selectbox('Modelo', model_options, index=model_options.index(st.session_state.model_name))

# O problema está aqui
with st.sidebar.form(key="form"):
    url = st.text_input("Paste the video URL here:")
    send = st.form_submit_button("Send")

if (not url) and (not send):
    st.info('Por favor, disponibilize uma URL do youtube.')
    st.stop()

video_infos = get_video_info(url, language, translation)
video_title = video_infos['title']
video_url = video_infos['url']
video_transcription = video_infos['transcription']
# O problema está aqui

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [AIMessage(content=f'Olá, estou aqui para falar sobre o vídeo {video_title}, encontrado em <{video_url}>. Pode me fazer qualquer pergunta ou requisição acerca dele.')]

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message('AI'):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message('Human'):
            st.write(message.content)

user_query = st.chat_input('Digite aqui sua pergunta sobre o vídeo...')
if '' != user_query is not None:
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message('Human'):
        st.markdown(user_query)
    with st.chat_message('AI'):
        resp = interpret_video(model_name, language, translation, url,
                                               user_query, video_transcription, st.session_state.chat_history)
        st.write_stream(resp)
    st.session_state.chat_history.append(AIMessage(content=resp))