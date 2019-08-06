#!/bin/bash 

function get_binaries () {
  wget https://github.com/raspberrypi/firmware/raw/master/boot/bootcode.bin
  wget https://github.com/raspberrypi/firmware/raw/master/boot/start.elf
}

function main () {
  get_binaries
}

main