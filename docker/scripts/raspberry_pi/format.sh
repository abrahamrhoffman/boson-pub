#!/bin/bash

function user_feedback () {
  echo "###########################"
  echo "# Boson: eMMC Format Tool #"
  echo "###########################"
}

function verify_root () {
  local USER=`whoami | sed 's/\\n//g'`
  if [[ "$USER" != "root" ]]
  then
    echo "Must execute as root. Try: 'sudo'"
      exit 1
  fi
}

function verify_drive () {
  local DRIVE=$1
  if [[ "$DRIVE" == "" ]]
  then
    echo "Must provide a drive. Example: '/dev/sdn'"
      exit 1
  fi
}

function wipe () {
  local DRIVE=$1
  echo -n "Wipe [${DRIVE}]      : "
  dd if=/dev/urandom of="$DRIVE" bs=1M count=1 &> /dev/null
  echo "Done"
}

function create () {
  local DRIVE=$1

  echo -n "Label [${DRIVE}]     : "
  parted -s "${DRIVE}" mklabel msdos
  echo "Done"

  echo -n "Partition [${DRIVE}] : "
  parted -a optimal -s $DRIVE mkpart primary fat32 0% 100%
  echo "Done"
}

function user_result () {
  local DRIVE=$1
  echo "######### Results #########"
  fdisk -l $DRIVE
}

function main () {
  local DRIVE=$1
  user_feedback
  verify_root
  verify_drive $DRIVE
  wipe $DRIVE
  create $DRIVE
  user_result $DRIVE
}

main $1