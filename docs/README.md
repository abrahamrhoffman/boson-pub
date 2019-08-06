# Dragonfly BMC Firmware

## Build Instructions

### Raspberry Pi

#### Raspberry Pi 2 B+ (32-Bit)

```
make CROSS_COMPILE=arm-linux-gnueabi- distclean
make CROSS_COMPILE=arm-linux-gnueabi- rpi_defconfig
make CROSS_COMPILE=arm-linux-gnueabi- 
```

#### Raspberry Pi 3 B+ (64-Bit)

```
make CROSS_COMPILE=aarch64-linux-gnu- distclean
make CROSS_COMPILE=aarch64-linux-gnu- rpi_3_defconfig
make CROSS_COMPILE=aarch64-linux-gnu-
```