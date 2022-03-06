FROM jenkins/slave:latest
USER root
WORKDIR /home/jenkins/agent
#installs python packages
RUN apt-get update && apt-get install -y \
	git \
	python3 \
	python3-pip
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install requests pandas openpyxl pytest

#run the python script
#CMD cd workspace
   #&& python3 Sampplepython.py