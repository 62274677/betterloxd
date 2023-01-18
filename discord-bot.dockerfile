FROM ubuntu:latest
ARG repo_url="https://github.com/62274677/betterloxd.git"
RUN apt update && apt upgrade
RUN apt install -y python3 git pip


# ADD "requirements.txt" .

RUN git clone ${repo_url} git_repo

RUN pip install -r "git_repo/requirements.txt"
# RUN pwd
RUN chmod +x "git_repo/run.sh"

# RUN echo "DEDBUG" 
# WORKDIR "/root/git_repo"

ENTRYPOINT [ "/bin/bash"]
CMD [ "/git_repo/run.sh", "/git_repo/" ]

