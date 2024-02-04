from youtube_transcript_api import YouTubeTranscriptApi as ytapi
from openai import OpenAI
from google import generativeai
import ollama
import requests
import os
from sys import platform
import time
import youtube_transcript_api
import re

"""OpenAI's API is not working for me, if you dont have any sort of issue on the API End and the program is returning an error feel free to open a issue reporting this incident and how to reach out so that we can fix 
it in real time.
Also will address a way to handle invalid inputted API Keys in the next version(s)..."""

#clear cli variables
clear_comm = "cls"
if platform in ["linux", "linux2"]:
	clear_comm = "clear"
elif platform == "darwin":
	clear_comm = "printf '\\33c\\e[3J'"


#user input for (L)LM selections
print("REMEMBER TO KEEP API KEYS TO YOURSELF AND NOT SHARE IT [Also during testing OpenAI did not work for me while Google did, it may work for you however].\n\nTo get started, Please select an AI Model API:\n1. Google Gemini[LIMITED REGIONS, SEE https://ai.google.dev/available_regions]\n2. OpenAI ChatGPT \n3. Ollama (Local) \n[More local and Networked (Large) Language Models to come when available or suggested]")
LM_selection = int(input("Select an AI in number: "))


#setup (L)LM API and write the API Key to text file of the same directory or read from them if it exists (Unless Ollama or other Local LMs were chosen), artificial slow down on read also so that the user reads...
if LM_selection == 1:
    try:
        with open("Google Gemini API KEY.txt", 'r') as geminiapikeyfile:
            if geminiapikeyfile.read() == "":
                with open("Google Gemini API KEY.txt", 'w') as geminiapikeyfile:
                    print("API key is not present in this file \nTo get started please setup an API Key here: https://makersuite.google.com/app/apikey \nand/or enter an existing API Key:")
                    geminiapikey = input()
                    geminiapikeyfile.write(geminiapikey)
                    geminiapikeyfile.close()
            else:
                with open("Google Gemini API KEY.txt", 'r') as geminiapikeyfile:
                    print("Google Gemini API Key seems to exist, retrieving to use...")
                    geminiapikey = geminiapikeyfile.read()
                    geminiapikeyfile.close()
                    time.sleep(2)
    except FileNotFoundError:
        with open("Google Gemini API KEY.txt", 'x') as geminiapikeyfile:
            print("First time setup has occured for this API \nTo get started please setup an API Key here: https://makersuite.google.com/app/apikey \nand/or enter an existing API Key:")
            geminiapikey = input()
            geminiapikeyfile.write(geminiapikey)
            geminiapikeyfile.close()
elif LM_selection == 2:
    try:
        with open("OpenAI ChatGPT API KEY.txt", 'r') as chatgptapikeyfile:
            if chatgptapikeyfile.read() == "":
                with open("OpenAI ChatGPT API KEY.txt", 'w') as chatgptapikeyfile:
                    print("API key is not present in this file \nTo get started please setup an API Key here: https://platform.openai.com/account/api-keys \nand/or enter an existing API Key:")
                    chatgptapikey = input()
                    chatgptapikeyfile.write(chatgptapikey)
                    chatgptapikeyfile.close()
            else:
                with open("OpenAI ChatGPT API KEY.txt", 'r') as chatgptapikeyfile:
                    print("ChatGPT API Key seems to exist, retrieving to use...")
                    chatgptapikey = chatgptapikeyfile.read()
                    chatgptapikeyfile.close()
                    time.sleep(2)
    except FileNotFoundError:
        with open("OpenAI ChatGPT API KEY.txt", 'x') as chatgptapikeyfile:
            print("First time setup has occured for this API \nTo get started please setup an API Key here: https://platform.openai.com/account/api-keys \nand/or enter an existing API Key:")
            chatgptapikey = input()
            chatgptapikeyfile.write(chatgptapikey)
            chatgptapikeyfile.close()
elif LM_selection == 3:
    print("continuing with Ollama..")
    time.sleep(2)

os.system(clear_comm)

#retrieve or setup Youtube Data v3 API key to allow for title to be given for the (L)LM, same way with the (L)LM setup one
global ytapikey
try:
    with open("youtubeapikey.txt", "r") as ytapikeyfile:
        if ytapikeyfile.read() == "":
            with open("youtubeapikey.txt", "w") as ytapikeyfile:
                print("File is empty. In order to retrieve the title of the video, you need to put a seperate api key that handles Youtube Data, see: https://developers.google.com/youtube/v3/getting-started and https://developers.google.com/youtube/registering_an_application (follow instructions on api key). \nInput it below:")
                ytapikey = input()
                ytapikeyfile.write(ytapikey)
                ytapikeyfile.close()
        else:
            with open("youtubeapikey.txt", "r") as ytapikeyfile:
                print("Youtube API Key seems to exist as well, retrieving...")
                ytapikey = ytapikeyfile.read()
                ytapikeyfile.close()
                time.sleep(2)
except FileNotFoundError:
    with open("youtubeapikey.txt", 'x') as ytapikeyfile:
        print("Now in order to retrieve the title of the video, you need to put a seperate api key that handles Youtube Data, see: https://developers.google.com/youtube/v3/getting-started and https://developers.google.com/youtube/registering_an_application (follow instructions on api key). \nInput it below:")
        ytapikey = input()
        ytapikeyfile.write(ytapikey)
        ytapikeyfile.close()

os.system(clear_comm)

#setting up (L)LM API Variables unless ollama or other local LMs were chosen.
if LM_selection == 2:
    cgptapi = OpenAI(api_key=chatgptapikey)
elif LM_selection == 3:
    print("Ollama was selected...")
elif LM_selection == 1:
    generativeai.configure(api_key=f"{geminiapikey}")
    gmodel = generativeai.GenerativeModel('gemini-pro')

#User input for a youtube URL  
youtube_url = input("Now Enter the Youtube Video URL to summarize: ")
global youtube_video_id
#using regular expression to filter any parameters
initial_youtube_video_id = youtube_url.strip(f"https://youtube.com/watch?v=")
youtube_video_id = re.sub("&(.*)", "", initial_youtube_video_id)

#retrieve video title of the id (using requests) and transcript (using youtube transcript api) and feed the message to the Model you chose and give the output later
def retrieve_video_title():
    title_retrieval = requests.get(f"https://youtube.googleapis.com/youtube/v3/videos", params={'part': 'snippet', 'id': f'{youtube_video_id}', 'key': f'{ytapikey}'})
    return title_retrieval.json()['items'][0]['snippet']['title']

try:
    initial_transcript = ytapi.get_transcript(f"{youtube_video_id}")
    transcript = """"""
    for transcript_retrieval in range(0, len(initial_transcript)):
        transcript += initial_transcript[transcript_retrieval]['text'] + "\n"
except youtube_transcript_api.TranscriptsDisabled:
    print("Seems like transcripts/subtitles are disabled via API or the video itself or they havent been generated, you can try manually inserting the transcript if there's a case of that")
    transcript = input("""> """)

if LM_selection == 2:
    cgptresponse = cgptapi.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"""Please read the following transcript of a youtube video and answer this: '{retrieve_video_title()}' \nThis is the transcript of the video: \n{transcript}"""}])
    print(cgptresponse.choices[0].message)
    input()
elif LM_selection == 1:
    google_ai_response = gmodel.generate_content(f"""Please read the following transcript of a youtube video and answer this: '{retrieve_video_title()}' \nThis is the transcript of the video: \n{transcript}""")
    print(google_ai_response.text)
    input()
elif LM_selection == 3:
    aimodelollama = input("AI Model to use?: ")
    response_ollama = ollama.chat(model=f"{aimodelollama}", messages=[{"role": "user", "content": f"""Please read the following transcript of a youtube video and answer this: '{retrieve_video_title()}' \nThis is the transcript of the video: \n{transcript}"""}])
    print(response_ollama['message']['content'])
    input()