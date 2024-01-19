ARG ARCH
FROM ${ARCH}alpine:3

RUN apk add \
    chromium \
    python3 \
    py3-pip \
    py3-numpy \
    py3-cryptography \
    py3-multidict \
    py3-yarl \
    chromium-chromedriver \
    && rm -rf /var/cache/* \
    && mkdir /var/cache/apk

WORKDIR /usr/src/app

COPY requirements.txt ./

# Cria um ambiente virtual
RUN python3 -m venv venv

# Ativa o ambiente virtual e instala as dependências
RUN source venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate

COPY examples/ ./examples

# Executa o script usando o interpretador do ambiente virtual
CMD ["venv/bin/python", "./examples/main.py"]
