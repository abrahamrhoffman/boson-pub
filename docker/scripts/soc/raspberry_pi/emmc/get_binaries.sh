#!/bin/bash 
function ensure_folder () {
  local DIRECTORY=$1
  rm -rf $DIRECTORY 2> /dev/null
  mkdir $DIRECTORY 2> /dev/null
}

function get_binaries () {
  wget https://github.com/raspberrypi/firmware/raw/master/boot/bootcode.bin \
    2> /dev/null
  wget https://github.com/raspberrypi/firmware/raw/master/boot/start.elf \
    2> /dev/null
}

function move_binaries () {
  local DIRECTORY=$1
  mv bootcode.bin ${DIRECTORY}
  mv start.elf ${DIRECTORY}
}

function main () {
  local DIRECTORY=$1
  ensure_folder $DIRECTORY
  get_binaries
  move_binaries $DIRECTORY
}

main $1