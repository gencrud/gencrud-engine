#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"


function init_env() {
  echo_purple "... check the environment workspace. It is the 'venv' folder.";

  ENV_PATH=$PWD"/venv/"

  if test -d $ENV_PATH; then
    echo_purple "Environment $ENV_PATH exist!"
    source $ENV_PATHh/bin/activate
  else
    echo_purple "... start to install environment ..." ; sleep 1;

    sudo apt-get update
    sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib virtualenv
    # sudo apt-get install postgis gdal-bin   # if you need postgis

    virtualenv --python=python3 venv
    source $ENV_PATH/bin/activate
    pip install -r $PWD"/gencrud/requirements.txt"
    echo_green "Virtualenv was created!\n\r"; sleep 1;
  fi
}