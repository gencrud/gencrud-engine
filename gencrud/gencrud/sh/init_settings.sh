#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"

DIR_NAME=${PWD##*/}
SETTINGS_PATH=$PWD"/gencrud/settings.py"

for param in "$@"
do
  echo_purple "... check the received parameter: $param"

  if [ "$param" == "create" ]; then
    init_settings $DIR_NAME
  fi

  if [ "$param" == "del" ] && test -f $SETTINGS_PATH; then
    rm -rf $PWD"/gencrud/settings.py"
    echo_red "settings.py was deleted from "$SETTINGS_PATH"!"
  fi

  if [ "$param" == "help" ] || [ "$param" == "-h" ]; then
    echo -e "\n# --------------------- HELP --------------------- #\r"
    echo_purple "Run commands from the 'PROJECT_NAME' folder:\n"
    echo -e "# create settings.py file\r"
    echo_green ". gencrud/gencrud/sh/init_settings.sh create\n"
    echo -e "# delete settings.py file\r"
    echo_green ". gencrud/gencrud/sh/init_settings.sh del\r"
    echo -e "# -------------------------------------------------- #\n"
  fi
done


function init_settings() {
  echo_purple "... check settings.py file";

  if test -f $SETTINGS_PATH; then
    echo_yellow "project_name: '$1' exists!\n\r"
  else
    echo_purple "... start to create settings.py ..." ; sleep 1;
    
    ROW="PROJECT_NAME = '$1'\nSITE_DOMAIN = '$1.com'\n"
    ROW_DB="DB_NAME = '$1'\nDB_USER = '$1'\nDB_PASSWORD = '{}888'.format('$1')\n"
    ROW_EMAIL="EMAIL_HOST_USER = '$1@emil.com'\nEMAIL_HOST_PASSWORD = '$1888'\n"
    ROWS=$ROW$ROW_DB$ROW_EMAIL
    echo -e $ROWS >> "${PWD}/gencrud/settings.py";

    echo_green "settings.py was created into ${PWD}/gencrud folder!\n\r"; sleep 1;
  fi
}



