subarch: mips64el_n32
target: stage1
version_stamp: openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsn32el
rel_type: default
profile: default/linux/mips/17.0/mipsel/n32
snapshot: @TIMESTAMP@
source_subpath: default/stage3-mips64el_n32-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
