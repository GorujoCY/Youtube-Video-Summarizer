# Youtube-Video-Summarizer
A CLI Youtube Video Summarizer written in Python using transcripts and YouTube video title (using the API) to retrieve a summary and feed a specific prompt to AI models (LM or LLM) either local or using API.
# Get started Windows
To get started for Windows, download the .exe binary I've created in the [Releases](https://github.com/GorujoCY/Youtube-Video-Summarizer/releases) and run the software, all the necessary packages are ready to use no setup should be needed
# Get Started Linux
For Linux it should be similar to Windows, [Download the binary (non .exe)](https://github.com/GorujoCY/Youtube-Video-Summarizer/releases) and its ready to use no setup should be needed
# Setup from source
To setup from source first open the command line to the directory you installed this repository and type `pip install -r requirements.txt` to install the necessary PyPI packages for the software to work, after that you can run it by double clicking the script or in the command line using `py(thon) youtubetranscriptsummarizer.py` 

For windows make sure you install(ed) python with PATH enabled before installation for those commands to work

For linux you may have to install `pip` seperately
# Current (Large) Language Models in
### API Based:
- OpenAI ChatGPT
- Google Gemini
### Local
- Ollama AI
# First time setup
When you run the script, first you choose the Language Model you want to use, Depending on the choice the next one is to setup an API Key if chosen one that communicates via the API (API Keys will be remembered in a text file), then you will be asked to setup and/or input the YouTube Data v3 API Key in order to retrieve the title of a YouTube video. Finally then refer to `Using it`
# Using it 
You will be prompted to choose a Language (AI) Model (they are not remembered in any case say APIs are down or different result of the AI Models). Then assuming the api key text files are not empty, the script will read the api key text file based on your AI model choice (if chosen a local model this will not be affected), Then it will check for the YouTube Data API v3 Api key text file and finally Prompt you to enter a YouTube video url, from there you enter a `youtube.com/watch` or `youtu.be` URL of a video. 

After entering the url, the YouTube Video ID is fetched in order to retrieve the transcript and title of the video from the API and then that data is being fed a standard prompt to the Language model you chose and Outputs the answer (or a summary).
# Known issues
- [ ] Contents on the file does not assume it is the actual token (because it doesnt do an api test to check, commited to fix in the next versions)
- [ ] During internal testing, OpenAI's API doesnt work, always being rate limited on my API Key (this is why I want the community to see for themselves and help fix any issues)
- [ ] Videos transcript sometimes dont always return, causing a "Transcript Disabled" error and puts the responsibility on the user because the transcript is there and acessible.

^ the cause is not very clear after testing (for example one video from one channel doesnt work but then another video from the same channel works) unfortunately but 

A workaround I can think of this is when prompted, copy the transcript manually, put it into a [single line converter](https://codebeautify.org/multiline-to-single-line) and paste it (I could make it easier but implementing a way to stop the loop without it intentionally stopping the user could be hard and frustrating every time my testing goes fine and not on the end product).
# Feedback
I'm open to suggestions for more online (supporting API) and local AI models and improvement. And with the software being GPLv3 would love to see the community implement something like GUI Versions.
