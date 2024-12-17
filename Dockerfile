FROM python:3.13.1

# Create unprevileged user to run app
RUN groupadd -g 1000 apprunner && \
    useradd -m -u 1000 -g apprunner apprunner

# Download dumb-init
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install dumb-init && \
## clear apt cache to reduce container image size
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Switch to custom user
USER apprunner

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["python", "main.py"]