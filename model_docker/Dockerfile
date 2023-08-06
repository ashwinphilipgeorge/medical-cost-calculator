FROM python:3.9
WORKDIR "/model_app"

RUN useradd -g root user

COPY main.py .
COPY requirements.txt .
COPY rfr_model.sav .

RUN pip install -r requirements.txt

USER user

EXPOSE 8000

CMD ["python","main.py"]