FROM python:3.10.3-bullseye

LABEL com.particlecounter.description="Particle Counter Web Server"
LABEL com.particlecounter.image.authors="Jerry Wu"

COPY . /app
WORKDIR /app
RUN apt-get update \
    && apt-get install -y unixodbc unixodbc-dev tdsodbc \
    && pip install --no-cache-dir -r requirements.txt \
    && echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini
RUN echo "[sql-server]\n\
Driver = FreeTDS\n\
Server = 192.168.3.120\n\
Database = ParticleCounter\n\
Port = 1433\n" >> /etc/odbc.ini

CMD ["flask", "run", "--host", "0.0.0.0"]