FROM ubuntu:latest
LABEL authors="vriel09"

ENTRYPOINT ["top", "-b"]