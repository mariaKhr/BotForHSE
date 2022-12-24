FROM python:3.11

RUN pip install aiohttp && pip install pyTelegramBotAPI

COPY ./main.py ./

CMD ["python",  "./main.py"]
