FROM python:3.13-slim

ARG SERVICE_NAME
ENV SERVICE_NAME=${SERVICE_NAME}

WORKDIR /app

COPY applications/${SERVICE_NAME}/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY applications ./applications
COPY shared ./shared

ENV PYTHONPATH=/app

EXPOSE 8080

CMD sh -c "python -m applications.${SERVICE_NAME}.app.main"