#!/bin/bash

SH_PATH=$PWD"/gencrud/gencrud/sh/"
source $SH_PATH"color.sh"


function init_app() {
  echo_purple "Check frontend 'app' folder";

  frontend_path=$PWD"/app/"
  zip_path=$PWD"/gencrud/gen/app.zip"

  if test -d $frontend_path; then
    echo_purple "Frontend path ${frontend_path} exist!"
  else
    echo_purple "... start to unzip archive ..." ; sleep 1;

    # sudo apt install unzip
    unzip $zip_path -d $PWD 
    
    echo_green "Frontend path was created! ${frontend_path}\n\r"; sleep 1;
  fi
}