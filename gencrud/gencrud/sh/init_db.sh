#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"
source $SH_PATH"create_superuser.sh"


DIR_NAME=${PWD##*/}
RUNSERVER_PATH=$PWD"/gencrud/manage.py"


for param in "$@"
do
  echo_purple "... check the received parameter: $param"

  if [ "$param" == "create_sqlite" ]; then
    init_sqlite $RUNSERVER_PATH $DIR_NAME".db"
    create_superuser
  fi

  if [ "$param" == "help" ] || [ "$param" == "-h" ]; then
    __help_init_db
  fi
done


function init_sqlite() {
  echo_purple "Try to create migrations and run project";
  run_path=$1
  db_name=$2

  if test -f $PWD/theme/$db_name; then
    echo_yellow "File $PWD/theme/$db_name exist!\n\r"; sleep 2;
  else
    echo_purple "... start to init project ..." ; sleep 2;
    
    python $run_path makemigrations
    python $run_path migrate

    echo_green "The 'settings.py' file was created into ${PWD}/gencrud folder!\n\r"; sleep 1;

  fi
}


function __help_init_db() {
  echo -e "\n# --------------------- HELP --------------------- #\r"
  echo_purple "Run commands from the 'PROJECT_NAME' folder:\n"
  echo -e "# create app, theme, DB \r"
  echo_green ". gencrud/gencrud/sh/init_theme.sh create\n"
  echo -e "# -------------------------------------------------- #\n"
}
