FROM python:3.9

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium



ARG repo_url="https://github.com/62274677/betterloxd.git"
RUN apt update && apt upgrade
RUN apt install -y python3 git pip wget 
# chromium-browser chromium-chromedriver snap snapd
# RUN snap install chromium
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
# RUN apt-get update
# RUN apt --fix-broken install
# RUN apt-get install google-chrome-stable -y


# RUN chromium-browser --headless --no-sandbox http://example.org/

# ADD "requirements.txt" .

RUN git clone ${repo_url} git_repo

RUN pip install -r "git_repo/requirements.txt"
# RUN pwd
RUN chmod +x "git_repo/run.sh"

# RUN echo "DEDBUG" 
# WORKDIR "/root/git_repo"

ENTRYPOINT [ "/bin/bash"]
CMD [ "/git_repo/run.sh", "/git_repo/" ]

