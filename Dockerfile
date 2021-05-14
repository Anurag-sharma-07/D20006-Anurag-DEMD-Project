FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app/
COPY ARIMA-Model-TSF.pkl .
COPY requirements.txt .
COPY ICICI-STOCK-PRICE.csv.
RUN pip install -r ./requirements.txt
COPY main.py /app/
CMD ["python", "main.py"]
