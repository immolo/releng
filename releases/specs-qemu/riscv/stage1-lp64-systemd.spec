subarch: rv64_lp64
target: stage1
version_stamp: systemd-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: default
profile: default/linux/riscv/20.0/rv64gc/lp64/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-rv64_lp64-systemd-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
