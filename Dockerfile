FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    chromium \
    chromium-driver \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libgtk-3-0 \
    fonts-liberation \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /app
RUN git clone https://github.com/Dagotra/selenium_1.git . && git checkout selenium_3
RUN pip install --no-cache-dit -r requirements.txt
EXPOSE 5000
CMD ["pytest", "-v", "-m", "not gui"]
