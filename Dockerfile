FROM python:3.13-slim
RUN apt-get update && apt-get install -y git
WORKDIR /app
RUN git clone https://github.com/Dagotra/selenium_1.git . && git checkout selenium_3
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["pytest", "-v", "-m", "not gui"]
