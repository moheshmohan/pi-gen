#!/bin/bash -e

rm -f "${ROOTFS_DIR}/etc/systemd/system/dhcpcd.service.d/wait.conf"

on_chroot << EOF
systemctl enable ssh
update-rc.d ssh enable
EOF
