subarch: hppa1.1
version_stamp: @TIMESTAMP@
target: livecd-stage2
rel_type: 23.0-default
profile: default/linux/hppa/23.0/hppa1.1
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/livecd-stage1-hppa1.1-@TIMESTAMP@
pkgcache_path: /var/tmp/catalyst/packages/23.0-default/installcd-stage2
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/volid: Gentoo hppa @TIMESTAMP@
livecd/bootargs: dokeymap
livecd/fstype: squashfs
livecd/iso: /var/tmp/catalyst/builds/23.0-default/install-hppa-minimal-@TIMESTAMP@.iso
livecd/type: gentoo-release-minimal

boot/kernel: hppa32 hppa64

boot/kernel/hppa32/sources: sys-kernel/gentoo-sources
boot/kernel/hppa32/config: @REPO_DIR@/releases/kconfig/hppa/hppa32.config
boot/kernel/hppa32/use:
	fbcon
	livecd
	png
	socks5
	truetype
	unicode
	usb

boot/kernel/hppa64/sources: sys-kernel/gentoo-sources
boot/kernel/hppa64/config: @REPO_DIR@/releases/kconfig/hppa/hppa64.config
boot/kernel/hppa64/gk_kernargs:
	--all-ramdisk-modules
	--kernel-ar=hppa64-unknown-linux-gnu-ar
	--kernel-as=hppa64-unknown-linux-gnu-as
	--kernel-cc=hppa64-unknown-linux-gnu-cc
	--kernel-ld=hppa64-unknown-linux-gnu-ld
	--kernel-nm=hppa64-unknown-linux-gnu-nm
	--kernel-objcopy=hppa64-unknown-linux-gnu-objcopy
	--kernel-objdump=hppa64-unknown-linux-gnu-objdump
	--kernel-ranlib=hppa64-unknown-linux-gnu-ranlib
	--kernel-readelf=hppa64-unknown-linux-gnu-readelf
	--kernel-strip=hppa64-unknown-linux-gnu-strip
boot/kernel/hppa64/use:
	fbcon
	livecd
	png
	socks5
	truetype
	unicode
	usb
	xml

boot/kernel/hppa32/extraversion: hppa32
boot/kernel/hppa64/extraversion: hppa64

livecd/unmerge:
	app-admin/eselect
	app-admin/eselect-lib-bin-symlink
	app-admin/eselect-pinentry
	app-admin/eselect-python
	app-admin/perl-cleaner
	app-admin/python-updater
	app-arch/cpio
	app-crypt/gnupg
	app-crypt/pinentry
	app-portage/portage-utils
	dev-build/libtool
	dev-libs/gmp
	app-text/build-docbook-catalog
	app-text/docbook-xml-dtd
	app-text/docbook-xsl-stylesheets
	app-text/openjade
	app-text/opensp
	app-text/po4a
	app-text/sgml-common
	dev-libs/elfutils
	dev-libs/eventlog
	dev-libs/libassuan
	dev-libs/pth
	dev-libs/libgpg-error
	dev-libs/libksba
	dev-libs/libpipeline
	dev-libs/libxml2
	dev-libs/libxslt
	dev-libs/mpc
	dev-libs/mpfr
	dev-libs/popt
	dev-util/gtk-doc-am
	dev-util/intltool
	dev-util/pkgconf
	net-misc/netifrc
	net-misc/rsync
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/groff
	sys-apps/help2man
	sys-apps/man-db
	sys-apps/sandbox
	sys-apps/tcp-wrappers
	sys-apps/texinfo
	sys-apps/miscfiles
	dev-build/autoconf
	dev-build/autoconf-wrapper
	dev-build/automake
	dev-build/automake-wrapper
	sys-devel/binutils
	sys-devel/binutils-hppa64
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/kgcc64
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/m4
	dev-build/make
	sys-devel/patch
	sys-kernel/genkernel
	sys-kernel/linux-headers
	sys-libs/db
	sys-libs/gdbm
	sys-libs/cracklib
	x11-misc/shared-mime-info

livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/usr/lib/dev-state
	/usr/lib/udev-state
	/usr/lib64/dev-state
	/usr/lib64/udev-state
	/root/.ccache
	/tmp
	/usr/diet/include
	/usr/diet/man
	/usr/include
	/usr/hppa*-unknown-linux-*
	/usr/include
	/usr/lib/X11/config
	/usr/lib/X11/doc
	/usr/lib/X11/etc
	/usr/lib/awk
	/usr/lib/ccache
	/usr/lib/gcc-config
	/usr/lib/nfs
	/usr/lib/perl5/site_perl
	/usr/lib/portage
	/usr/lib64/X11/config
	/usr/lib64/X11/doc
	/usr/lib64/X11/etc
	/usr/lib64/awk
	/usr/lib64/ccache
	/usr/lib64/gcc-config
	/usr/lib64/nfs
	/usr/lib64/perl5/site_perl
	/usr/lib64/portage
	/usr/local
	/usr/portage
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/binutils-data
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
	/usr/share/gcc-data
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/libtool
	/usr/share/locale
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/src
	/var/cache
	/var/empty
	/var/lib/portage
	/var/lock
	/var/log
	/var/run
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/env.d/05binutils
	/etc/env.d/05gcc
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/genkernel.conf
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/cpp
	/root/.bash_history
	/root/.viminfo
	/usr/bin/*.static
	/usr/bin/fsck.cramfs
	/usr/bin/fsck.minix
	/usr/bin/mkfs.bfs
	/usr/bin/mkfs.cramfs
	/usr/bin/mkfs.minix
	/usr/bin/addr2line
	/usr/bin/ar
	/usr/bin/as
	/usr/bin/audioctl
	/usr/bin/c++*
	/usr/bin/cc
	/usr/bin/cjpeg
	/usr/bin/cpp
	/usr/bin/djpeg
	/usr/bin/ebuild
	/usr/bin/egencache
	/usr/bin/emerge
	/usr/bin/emerge-webrsync
	/usr/bin/emirrordist
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
	/usr/bin/gcc*
	/usr/bin/genkernel
	/usr/bin/gprof
	/usr/bin/i386-gentoo-linux-uclibc-*
	/usr/bin/i386-pc-linux-*
	/usr/bin/jpegtran
	/usr/bin/ld
	/usr/bin/libpng*
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback*
	/usr/bin/portageq
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/size
	/usr/bin/powerpc-unknown-linux-gnu-*
	/usr/bin/powerpc64-unknown-linux-gnu-*
	/usr/bin/sparc-unknown-linux-gnu-*
	/usr/bin/sparc64-unknown-linux-gnu-*
	/usr/bin/strings
	/usr/bin/strip
	/usr/bin/tbz2tool
	/usr/bin/x86_64-pc-linux-gnu-*
	/usr/bin/xpak
	/usr/bin/yacc
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/perl5/site_perl
	/usr/lib*/gcc-lib/*/*/libgcj*
	/usr/bin/archive-conf
	/usr/bin/dispatch-conf
	/usr/bin/emaint
	/usr/bin/env-update
	/usr/bin/etc-update
	/usr/bin/fb*
	/usr/bin/fixpackages
	/usr/bin/quickpkg
	/usr/bin/regenworld
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
	/usr/share/misc/*.old
