FROM alpine:3.20
RUN apk update
RUN apk add python3
RUN apk add py3-pip
WORKDIR /orders
COPY requirements.txt .
COPY orders-server.py .
RUN python3 -m venv ordersenv
ENV PATH="/orders/ordersenv/bin:$PATH"
RUN pip install -r requirements.txt
CMD ["python3", "orders-server.py"]


