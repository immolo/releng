subarch: i486
version_stamp: openrc-@TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/x86/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage3-i486-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/use:
	alsa
	compile-locales
	fbcon
	ipv6
	livecd
	modules
	ncurses
	nls
	pam
	portaudio
	readline
	socks5
	ssl
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-accessibility/espeakup
	app-admin/hddtemp
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-misc/livecd-tools
	app-misc/screen
	app-misc/tmux
	app-portage/cpuid2cpuflags
	app-portage/mirrorselect
	app-text/wgetpaste
	media-gfx/fbgrab
	media-sound/alsa-utils
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-proxy/tsocks
	net-wireless/b43-fwcutter
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/netplug
	sys-apps/pciutils
	sys-apps/pcmciautils
	sys-apps/sdparm
	sys-apps/usbutils
	sys-auth/ssh-import-id
	sys-block/parted
	sys-block/partimage
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-power/acpid
	www-client/links
