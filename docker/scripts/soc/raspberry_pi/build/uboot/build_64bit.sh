# 64-Bit Raspberry Pi 3 B+
make CROSS_COMPILE=aarch64-linux-gnu- distclean
make CROSS_COMPILE=aarch64-linux-gnu- rpi_3_defconfig
make -j $(nproc) CROSS_COMPILE=aarch64-linux-gnu-