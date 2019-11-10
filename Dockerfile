FROM snakepacker/python:all as builder

RUN python3.7 -m venv /usr/share/python3/app

ENV PATH="/usr/share/python3/app/bin:${PATH}"

ADD setup.py /tmp/
ADD requirements.txt /tmp/

RUN pip install -e /tmp

FROM snakepacker/python:3.7 as app

COPY --from=builder /usr/share/python3/app \
    /usr/share/python3/app

ENV PATH="/usr/share/python3/app/bin:${PATH}"
ENV PYTHONPATH=".:${PYTHONPATH}"

ADD ./service/ /mnt/service/

WORKDIR /mnt

EXPOSE 80

CMD ["python3", "service/__main__.py"]
