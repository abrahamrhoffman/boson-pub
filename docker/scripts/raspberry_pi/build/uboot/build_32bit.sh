# 32-Bit Raspberry Pi 2 B+
make CROSS_COMPILE=arm-linux-gnueabi- distclean
make CROSS_COMPILE=arm-linux-gnueabi- rpi_defconfig
make -j $(nproc) CROSS_COMPILE=arm-linux-gnueabi-