FROM python

COPY . /app
WORKDIR /app
RUN apt-get update \
    && apt-get install -y unixodbc unixodbc-dev tdsodbc \
    && pip install --no-cache-dir -r requirements.txt \
    && echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/arm-linux-gnueabi/odbc/libtdsodbc.so\n\
Setup = /usr/lib/arm-linux-gnueabi/odbc/libtdsS.so" >> /etc/odbcinst.ini \
&& echo "[sql-server]\n\
Driver = FreeTDS\n\
Server = 192.168.3.120\n\
Database = ParticleCounter\n\
Port = 1433\n" >> /etc/odbc.ini

CMD ["flask", "run", "--host", "0.0.0.0"]