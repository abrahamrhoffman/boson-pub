#!/bin/bash

function verify_root () {
  local USER=`whoami | sed 's/\\n//g'`
  if [[ "$USER" != "root" ]]
  then
    echo "Must execute as root. Try: sudo"
      exit 1
  fi
}

function wipe () {
  echo -n "Wiping $1 ... "
  dd if=/dev/urandom of="$1" bs=1M count=1 &> /dev/null
  echo "Done"
}

function format () {
  sudo parted 
}

function main () {
  verify_root
  wipe $1
}

main $1