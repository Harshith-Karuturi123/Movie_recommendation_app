# Movie_recommendation_app
We will use GenAI model like google gemini to suggest a movie similar to the user input

# App link
https://movierecommendationapp-wmxitxf7kl5cwgd7evbefb.streamlit.app/

# How does it work:
Sign in to github
1.	Create Repo
2.	gitbash
3.	cd d:
4.	Go to git Repo (Green button Code)-> Copy the url of repo (HTTPS)
5.	git clone <repo_URL>
6.	Now the git repo gets made/cloned in the D: drive
7.	cd match_resume.ai/ (went to the actual folder - main to open VScode there)
8.	code .
9.	IN vscode now you will land on the project match_resume.ai/ , click on newfile
10.	create .env file (to store api etc.) GOOGLE-GEMINI-API = "api_key"
11.	create requirements.txt (Google colab comes with preinstalled libraries, but not vscode)
12.	streamlit, pypdf, google-generativeai, (now we want to run the apikey to run locally before it goes global) so python-dotenv, langchaiin
13.	Click on terminal (powershell opens)(convert it to Gitbash)
14.	Now lets create the virtual env
15.	Before that optionally we can write notes in read me
16.	Check python version
17.	python -m venv .venv (create venv)
18.	source .venv/Scripts/activate(Windows) or source .venv/bin/activate (works for macos)
19.	
20.	pip install -r requirements.txt
21.	create app.py
22.	Write or copy the code
23.	Run the app file (python run app.py) - Optional
24.	lets say you want to test the code written so far use command streamlit run app.py
25.	for the first time it will ask for some credentials
26.	once you are done running the app go to gitbash
27.	activate venv (if needed) then type git init
28.	git add. (add everything)
29.	git commit -m "Final-Commit"
30.	If running git the first time: git config --global user.email git config --global user.name <user_name>
31.	git push origin main
32.	git commit -m "Final-Commit"
33.	git push origin main
34.	GO to streamlit and login using GitHub , click on create app

