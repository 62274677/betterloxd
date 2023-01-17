FROM python:3.9
ARG repo_url="https://github.com/62274677/betterloxd.git"
RUN apt update && apt upgrade


# ADD "requirements.txt" .

RUN git clone ${repo_url} git_repo
RUN pip install -r "git_repo/requirements.txt"
# RUN echo "DEDBUG"

ENTRYPOINT [ "git_repo/run.sh" ]


