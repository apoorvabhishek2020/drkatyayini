# FROM python:3.10.7-alpine
FROM python:latest
EXPOSE 8000/tcp
WORKDIR /app
COPY . .
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN apk add --no-cache --upgrade bash
RUN pip install -r requirements.txt
RUN chmod a+x initscript.sh
CMD ["./initscript.sh"]