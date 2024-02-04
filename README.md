# Youtube-Video-Summarizer
A Youtube Video Summarizer written in Python using transcripts and YouTube video title (using the API) to retrieve a summary and feed a specific prompt to AI models (LM or LLM) either local or using API
# Get started
To get started for Windows download the .exe binaries I've created in the [Releases](https://github.com/GorujoCY/Youtube-Video-Summarizer/releases) and run the software, all the necessary packages are ready to use no setup should be needed 

[BINARIES NOT IMPLEMENTED YET, STATEMENT MAY CHANGE]
# Setup from source
To setup from source first open the command line to the directory you installed this repository and type `pip install -r requirements.txt` to install the necessary PyPI packages for the sopftware to work, after that you can run it by double clicking the script or in the command line using `py(thon) youtubetranscriptsummarizer.py` 

For windows make sure you install(ed) python with PATH enabled before installation for those commands to work
# First time setup

# Known issues
- [ ] Contents on the file does not assume it is the actual token (because it doesnt do an api test to check, commited to fix in the next versions)
- [ ] During internal testing, OpenAI's API doesnt work, always being rate limited on my API Key (this is why I want the community to see for themselves and help fix any issues)
