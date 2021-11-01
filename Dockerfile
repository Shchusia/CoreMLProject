FROM python:3.9-slim-buster

ARG work_dir="/app/"
WORKDIR $work_dir
COPY . .


RUN apt-get update

# ###################
# ### if use cron ###
# ###################
RUN apt-get -y install cron

RUN chmod -v +x ./cron.sh
RUN ./cron.sh $work_dir

RUN chmod -v +x ./docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]

RUN touch /var/log/cron.log

# in time CMD command
# CMD cron && ...
# ###################

# ##########################
# ### for db bulk insert ###
# ##########################
RUN ACCEPT_EULA=Y apt install -y mssql-tools unixodbc
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN ln -s /opt/mssql-tools/bin/bcp /bin/bcp
CMD source ~/.bashrc
# ##########################

RUN pip install --upgrade --no-cache-dir -r requirements/base.txt

# run rabbit
# CMD python ./app_mq.py

# run rest
# EXPOSE 5000 8000
# CMD gunicorn  app_rest:dispatcher --workers 4 --bind 0.0.0.0:5000 --log-level=DEBUG --reload --timeout 100 --preload