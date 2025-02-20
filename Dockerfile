FROM hitokizzy/geezram:slim-buster

COPY . /app/
WORKDIR /app/

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && pip3 install --no-cache-dir -U -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
CMD bash start.sh
