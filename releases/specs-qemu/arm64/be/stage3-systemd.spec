subarch: aarch64_be
version_stamp: systemd-@TIMESTAMP@
target: stage3
rel_type: default
profile: default/linux/arm64/17.0/big-endian/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage1-aarch64_be-systemd-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
interpreter: /usr/bin/qemu-aarch64_be