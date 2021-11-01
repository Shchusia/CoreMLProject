# cron_functions

[назад](../README.md)

функции крона которые необходимо выполнять периодично

### связанные файлы 
- cron - для описания задач какие надо выполнять а cron-е в стандратном виде крона
- cron.sh - подготавливает функции для из файла `cron` для выполнения в контейнере
- docker-entrypoint.sh -

### _!!! обязательно в `cron` файлах !!!_

Следите чтоб все файлы настроек `cron` файлов (файлы 👆): 
- кодировку utf-8 
- имели `формат конца строк` был `Unix(LF)` 
- все файлы имели вконце пустую строку

### _!!! обязательно в `Dockerfile` !!!_

```dockerfile
RUN apt-get -y install cron

RUN chmod -v +x ./cron.sh
RUN ./cron.sh $work_dir

RUN chmod -v +x ./docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]

RUN touch /var/log/cron.log

CMD cron && # остальные ваши команды
```


### _!!! обязательно в исполняемых файлах!!!_

Первые строки в кронфайлах если будет необходимость использовать функционал какой-то из данного репозитория
```python
import sys
from pathlib import Path

# block for use files base directory in docker runner
directory = Path(__file__)
sys.path.insert(0, str(directory.parent.absolute().parent))

```