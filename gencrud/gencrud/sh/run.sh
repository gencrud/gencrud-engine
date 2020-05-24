#!/bin/bash

source $PWD"/gencrud/gencrud/sh/color.sh"
source venv/bin/activate

RUNSERVER_PATH=$PWD'/gencrud/manage.py'

if test -f $RUNSERVER_PATH; then
  python $RUNSERVER_PATH runserver
  echo_green "Project ${path} RUN! http://localhost:8000/\n\r"
 else
  	echo_red "File doesn't found\n\r"
fi
