subarch: ppc
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: default
profile: default/linux/ppc/17.0/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-ppc-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
