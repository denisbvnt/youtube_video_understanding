from logging import exception
import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.output_parsers import StrOutputParser
from models import load_model
from templates import define_prompt_template


def get_video_title(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')
    link = soup.find_all(name="title")[0]
    title = str(link)
    title = title.replace("<title>","")
    title = title.replace("</title>","")
    return title

def get_video_info(url, language='pt', translation=None):
    video_loader = YoutubeLoader.from_youtube_url(url,
                                                  language=language,
                                                  translation=translation)
    infos = video_loader.load()
    transcription = infos[0].page_content
    title = get_video_title(url)
    infos = {'title': title, 'url': url, 'transcription': transcription}
    return infos

def interpret_video(model_name, language, translation, url, query, video_transcription, chat_history):
    try:
        llm = load_model(model_name)
        prompt_template = define_prompt_template(llm)
        chain = prompt_template | llm | StrOutputParser()
        result = chain.stream({"transcription": video_transcription, "query": query, 'chat_history': chat_history})
        return result
    except exception as e:
        print('Error to load trancription.')
        return e