# 32-Bit Raspberry Pi 2 B+
make CROSS_COMPILE=arm-linux-gnueabi- distclean
make CROSS_COMPILE=arm-linux-gnueabi- rpi_defconfig
make CROSS_COMPILE=arm-linux-gnueabi- 

# 64-Bit Raspberry Pi 3 B+
make CROSS_COMPILE=aarch64-linux-gnu- distclean
make CROSS_COMPILE=aarch64-linux-gnu- rpi_3_defconfig
make CROSS_COMPILE=aarch64-linux-gnu- 