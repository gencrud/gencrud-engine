#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"


DIR_NAME=${PWD##*/}
RUNSERVER_PATH=$PWD"/gencrud/manage.py"


for param in "$@"
do
  echo_purple "... check the received parameter: $param"

  if [ "$param" == "core" ]; then
    upgrade_gencrud_core
  fi

  if [ "$param" == "help" ] || [ "$param" == "-h" ]; then
    __help_upgrade
  fi
  
done


function upgrade_gencrud_core() {
  echo_purple "Try to UPGRADE"; sleep 1;

  if test -f $PWD/upgrade.zip; then
    
    if test -d $PWD/upgrade; then
      rm -fr $PWD/upgrade;
    fi

    echo_purple "... start to upgrade project ..." ; sleep 1;
    
    mkdir $PWD/__BACKUP__
    unzip "upgrade.zip" -d $PWD

    sleep 1;
    echo_purple "move root-files into __BACKUP__"
    mv $PWD/install.sh __BACKUP__
    mv $PWD/README.md __BACKUP__
    mv $PWD/.gitignore __BACKUP__
    echo_green "new files reciev from upgrade.zip(1)"
    mv $PWD/upgrade/install.sh install.sh
    mv $PWD/upgrade/README.md README.md
    mv $PWD/upgrade/.gitignore .gitignore

    sleep 1;
    echo_purple "move manage.py, requirements.txt into __BACKUP__/gencrud";
    mkdir $PWD/__BACKUP__/gencrud
    mv $PWD/gencrud/manage.py __BACKUP__/gencrud/manage.py
    mv $PWD/gencrud/requirements.txt __BACKUP__/gencrud/requirements.txt
    echo_green "new files reciev from upgrade.zip(2)"
    mv $PWD/upgrade/gencrud/manage.py $PWD/gencrud/manage.py
    mv $PWD/upgrade/gencrud/requirements.txt $PWD/gencrud/requirements.txt

    sleep 1;
    echo_purple "move gen, gencrud into __BACKUP__/gencrud/**"
    mkdir $PWD/__BACKUP__/gencrud/gen
    mkdir $PWD/__BACKUP__/gencrud/gencrud
    mv $PWD/gencrud/gen __BACKUP__/gencrud
    mv $PWD/gencrud/gencrud __BACKUP__/gencrud
    echo_green "new files reciev from upgrade.zip(3)"
    mv $PWD/upgrade/gencrud/gen $PWD/gencrud/gen
    mv $PWD/upgrade/gencrud/gencrud $PWD/gencrud/gencrud
    rm -rf $PWD/upgrade

    echo_green "Upgade was finished!\n\r"; sleep 1;

    # todo: create backup_db. After aplly this code
    echo -e "# Next, create backup db! After aplly this commands\r"
    echo_green "python $RUNSERVER_PATH makemigrations\r"
    echo_green "python $RUNSERVER_PATH migrate\n"
  else
    echo_red "The 'upgrade.zip' archive doesn't exist in the root folder!\n\r"; sleep 2;    
  fi
}


function __help_upgrade() {
  echo -e "\n# --------------------- HELP --------------------- #\r"
  echo_purple "Run commands from the 'PROJECT_NAME' folder:\n"

  echo -e "# upgrade gencrud/gen, gencrud/gencrud folders and main files into the root\r"
  echo_green ". gencrud/gencrud/sh/upgrade.sh engine\n"
  echo -e "# -------------------------------------------------- #\n"
}
