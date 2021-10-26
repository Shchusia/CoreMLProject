FROM python:3.9-slim-buster

ARG work_dir="/app/"
WORKDIR $work_dir
COPY . .


RUN apt-get update

