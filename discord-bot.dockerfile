FROM ubuntu:latest
ARG repo_url="https://github.com/62274677/betterloxd.git"
RUN apt update && apt upgrade
RUN apt install -y python3 git pip wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt --fix-broken install
RUN apt-get install google-chrome-stable -y

# ADD "requirements.txt" .

RUN git clone ${repo_url} git_repo

RUN pip install -r "git_repo/requirements.txt"
# RUN pwd
RUN chmod +x "git_repo/run.sh"

# RUN echo "DEDBUG" 
# WORKDIR "/root/git_repo"

ENTRYPOINT [ "/bin/bash"]
CMD [ "/git_repo/run.sh", "/git_repo/" ]

