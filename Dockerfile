# Includes python3 and graphviz

FROM fnndsc/ubuntu-python3
LABEL maintainer="sjkillen@ualberta.ca"

RUN apt-get -qq update
RUN apt-get -qq install graphviz
RUN pip3 install graphviz frozendict more-itertools

ENTRYPOINT ["python3"]
