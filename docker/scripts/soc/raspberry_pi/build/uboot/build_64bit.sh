# 64-Bit Raspberry Pi 3 B+
function build () {
  local DIRECTORY=$1
  make --directory ${DIRECTORY} \
    CROSS_COMPILE=aarch64-linux-gnu- distclean
  make --directory ${DIRECTORY} \
    CROSS_COMPILE=aarch64-linux-gnu- rpi_3_defconfig
  make --directory ${DIRECTORY} \
       -j $(nproc) CROSS_COMPILE=aarch64-linux-gnu-
}

function main () {
  local DIRECTORY=$1
  build $DIRECTORY
}

main $1