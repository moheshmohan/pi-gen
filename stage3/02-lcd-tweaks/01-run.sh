#!/bin/bash -e


install -v -d					"${ROOTFS_DIR}/etc/modprobe.d"
install -v -m 644 files/etc/modprobe.d/fbtft.conf		"${ROOTFS_DIR}/etc/modprobe.d/"
install -v -m 644 files/etc/modules		"${ROOTFS_DIR}/etc/"


install -v -d					"${ROOTFS_DIR}/etc/modules-load.d"
install -v -m 600 files/etc/modules-load.d/fbtft.conf	"${ROOTFS_DIR}/etc/modules-load.d/"

install -v -d					"${ROOTFS_DIR}/usr/share/X11/xorg.conf.d"
install -v -m 600 files/usr/share/X11/xorg.conf.d/99-fbdev.conf	"${ROOTFS_DIR}/usr/share/X11/xorg.conf.d/"

install -v -m 655 files/home/*.* "${ROOTFS_DIR}/home/pi/"
