#!/bin/bash

while read line; do
  IFS=' ' read -r -a arr <<< "$line"
  arr=("${arr[@]:0:5}" "root" "${arr[@]:5}")
  if [[ "$line" == *"python"* ]]; then
    arr[7]="$1""${arr[7]}"
  fi
  nline=$( IFS=$' '; echo "${arr[*]}" )
  echo "$nline >> /var/log/cron.log " >> /etc/crontab;
done < cron

