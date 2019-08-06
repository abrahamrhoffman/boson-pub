# 32-Bit Raspberry Pi 2 B+
function build () {
  local DIRECTORY=$1
  make --directory ${DIRECTORY} \
    CROSS_COMPILE=arm-linux-gnueabi- distclean
  make --directory ${DIRECTORY} \
    CROSS_COMPILE=arm-linux-gnueabi- rpi_defconfig
  make --directory ${DIRECTORY} \
       -j $(nproc) CROSS_COMPILE=arm-linux-gnueabi-
}

function main () {
  local DIRECTORY=$1
  build $DIRECTORY
}

main $1