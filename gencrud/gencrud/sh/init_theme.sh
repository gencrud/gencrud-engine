#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"
source $SH_PATH"init_app.sh"
source $SH_PATH"init_db.sh"
source $SH_PATH"create_superuser.sh"


DIR_NAME=${PWD##*/}


for param in "$@"
do
  echo_purple "... check the received parameter: $param"

  if [ "$param" == "create" ]; then
    init_theme
  fi

  if [ "$param" == "help" ] || [ "$param" == "-h" ]; then
    __help_init_theme
  fi
done


function init_theme() {
  init_app

  echo_purple "... check theme workspace:";

  theme_path=$PWD"/theme/"
  zip_path=$PWD"/gencrud/gen/theme.zip"

  if test -d $theme_path; then
    echo_yellow "Theme ${theme_path} exist!\r\n"
  else
    echo_purple "... start to unzip archive ..."; sleep 2;

    # sudo apt install unzip
    unzip $zip_path -d $PWD
    
    echo_green "Theme was created! ${theme_path}\r\n"
  fi
}


function __help_init_theme() {
  echo -e "\n# --------------------- HELP --------------------- #\r"
  echo_purple "Run commands from the 'PROJECT_NAME' folder:\n"
  echo -e "# create app, theme, DB \r"
  echo_green ". gencrud/gencrud/sh/init_theme.sh create\n"
  echo -e "# -------------------------------------------------- #\n"
}