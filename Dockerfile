FROM python:3

ADD src /src

RUN pip install coverage

CMD [ "python", "./src/CalculatorTests.py" ]

CMD [ "python", "./src/StatisticsTests.py" ]
