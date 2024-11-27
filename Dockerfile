FROM python:3.9

WORKDIR /app
COPY . /app

RUN /bin/bash -c "chmod +x scripts/setup.sh && ./scripts/setup.sh && \
    chmod +x scripts/google_chrome.sh && ./scripts/google_chrome.sh && \
    chmod +x scripts/install_jdk_maven.sh && ./scripts/install_jdk_maven.sh && \
    chmod +x scripts/sql_server_driver.sh && ./scripts/sql_server_driver.sh"

COPY . .