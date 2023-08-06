FROM python:3.9-slim
RUN useradd -u 8877 user
WORKDIR /app

COPY streamlit.py .
RUN pip install streamlit==1.25.0
RUN pip install protobuf==3.20.0

EXPOSE 8501

USER user
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit.py"]
