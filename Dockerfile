FROM python
RUN pip install telebot pytube moviepy
WORKDIR /bot
COPY . /bot
CMD ["python", "bot.py"]
