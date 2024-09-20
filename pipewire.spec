#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : pipewire
Version  : 1.2.4
Release  : 118
URL      : https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/1.2.4/pipewire-1.2.4.tar.gz
Source0  : https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/1.2.4/pipewire-1.2.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: pipewire-bin = %{version}-%{release}
Requires: pipewire-config = %{version}-%{release}
Requires: pipewire-data = %{version}-%{release}
Requires: pipewire-lib = %{version}-%{release}
Requires: pipewire-license = %{version}-%{release}
Requires: pipewire-locales = %{version}-%{release}
Requires: pipewire-services = %{version}-%{release}
Requires: jack2
Requires: pulseaudio
BuildRequires : SDL2-dev
BuildRequires : bluez-dev
BuildRequires : buildreq-meson
BuildRequires : libcap-dev
BuildRequires : libsndfile-dev
BuildRequires : libusb-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(systemd)
BuildRequires : readline-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PipeWire
[PipeWire](https://pipewire.org) is a server and user space API to
deal with multimedia pipelines. This includes:

%package bin
Summary: bin components for the pipewire package.
Group: Binaries
Requires: pipewire-data = %{version}-%{release}
Requires: pipewire-config = %{version}-%{release}
Requires: pipewire-license = %{version}-%{release}
Requires: pipewire-services = %{version}-%{release}

%description bin
bin components for the pipewire package.


%package config
Summary: config components for the pipewire package.
Group: Default

%description config
config components for the pipewire package.


%package data
Summary: data components for the pipewire package.
Group: Data

%description data
data components for the pipewire package.


%package dev
Summary: dev components for the pipewire package.
Group: Development
Requires: pipewire-lib = %{version}-%{release}
Requires: pipewire-bin = %{version}-%{release}
Requires: pipewire-data = %{version}-%{release}
Provides: pipewire-devel = %{version}-%{release}
Requires: pipewire = %{version}-%{release}

%description dev
dev components for the pipewire package.


%package extras
Summary: extras components for the pipewire package.
Group: Default

%description extras
extras components for the pipewire package.


%package lib
Summary: lib components for the pipewire package.
Group: Libraries
Requires: pipewire-data = %{version}-%{release}
Requires: pipewire-license = %{version}-%{release}

%description lib
lib components for the pipewire package.


%package license
Summary: license components for the pipewire package.
Group: Default

%description license
license components for the pipewire package.


%package locales
Summary: locales components for the pipewire package.
Group: Default

%description locales
locales components for the pipewire package.


%package services
Summary: services components for the pipewire package.
Group: Systemd services
Requires: systemd

%description services
services components for the pipewire package.


%prep
%setup -q -n pipewire-1.2.4
cd %{_builddir}/pipewire-1.2.4
pushd ..
cp -a pipewire-1.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726859894
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dpipewire-jack=enabled \
-Dudevrulesdir="/usr/lib/udev/rules.d" \
-Dlibcamera=disabled \
-Dsession-managers=[] \
-Davahi=disabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dpipewire-jack=enabled \
-Dudevrulesdir="/usr/lib/udev/rules.d" \
-Dlibcamera=disabled \
-Dsession-managers=[] \
-Davahi=disabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/pipewire
cp %{_builddir}/pipewire-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pipewire/13641f6e59f451fcd8b6f92b449b91e4265854a5 || :
cp %{_builddir}/pipewire-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pipewire/b20949a01ecd5fc139d843db8a3e3b66b6ab8623 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang pipewire
## install_append content
rm -fv %{buildroot}*/usr/lib64/pipewire-*/jack/libjack.so*
rm -fv %{buildroot}*/usr/lib64/pipewire-*/jack/libjacknet.so*
rm -fv %{buildroot}*/usr/lib64/pipewire-*/jack/libjackserver.so*
mkdir -p %{buildroot}/usr/lib/systemd/user/sockets.target.wants
ln -s ../pipewire.socket %{buildroot}/usr/lib/systemd/user/sockets.target.wants
ln -s ../pipewire-pulse.socket %{buildroot}/usr/lib/systemd/user/sockets.target.wants
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pipewire
/V3/usr/bin/pw-cat
/V3/usr/bin/pw-cli
/V3/usr/bin/pw-config
/V3/usr/bin/pw-container
/V3/usr/bin/pw-dot
/V3/usr/bin/pw-dump
/V3/usr/bin/pw-link
/V3/usr/bin/pw-loopback
/V3/usr/bin/pw-metadata
/V3/usr/bin/pw-mididump
/V3/usr/bin/pw-mon
/V3/usr/bin/pw-profiler
/V3/usr/bin/pw-reserve
/V3/usr/bin/pw-top
/V3/usr/bin/spa-acp-tool
/V3/usr/bin/spa-inspect
/V3/usr/bin/spa-json-dump
/V3/usr/bin/spa-monitor
/V3/usr/bin/spa-resample
/usr/bin/pipewire
/usr/bin/pipewire-aes67
/usr/bin/pipewire-avb
/usr/bin/pipewire-pulse
/usr/bin/pw-cat
/usr/bin/pw-cli
/usr/bin/pw-config
/usr/bin/pw-container
/usr/bin/pw-dot
/usr/bin/pw-dsdplay
/usr/bin/pw-dump
/usr/bin/pw-encplay
/usr/bin/pw-jack
/usr/bin/pw-link
/usr/bin/pw-loopback
/usr/bin/pw-metadata
/usr/bin/pw-mididump
/usr/bin/pw-midiplay
/usr/bin/pw-midirecord
/usr/bin/pw-mon
/usr/bin/pw-play
/usr/bin/pw-profiler
/usr/bin/pw-record
/usr/bin/pw-reserve
/usr/bin/pw-top
/usr/bin/pw-v4l2
/usr/bin/spa-acp-tool
/usr/bin/spa-inspect
/usr/bin/spa-json-dump
/usr/bin/spa-monitor
/usr/bin/spa-resample

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/90-pipewire-alsa.rules

%files data
%defattr(-,root,root,-)
/usr/share/alsa-card-profile/mixer/paths/analog-input-aux.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-dock-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-fm.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-front-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-headphone-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-headset-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-internal-mic-always.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-internal-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-linein.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-mic-line.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-mic.conf.common
/usr/share/alsa-card-profile/mixer/paths/analog-input-rear-mic.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-tvtuner.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input-video.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input.conf
/usr/share/alsa-card-profile/mixer/paths/analog-input.conf.common
/usr/share/alsa-card-profile/mixer/paths/analog-output-chat.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output-headphones-2.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output-headphones.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output-lineout.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output-mono.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output-speaker-always.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output-speaker.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output.conf
/usr/share/alsa-card-profile/mixer/paths/analog-output.conf.common
/usr/share/alsa-card-profile/mixer/paths/audigy-analog-output-mirror.conf
/usr/share/alsa-card-profile/mixer/paths/audigy-analog-output.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-0.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-1.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-10.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-2.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-3.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-4.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-5.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-6.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-7.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-8.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-9.conf
/usr/share/alsa-card-profile/mixer/paths/iec958-stereo-input.conf
/usr/share/alsa-card-profile/mixer/paths/iec958-stereo-output.conf
/usr/share/alsa-card-profile/mixer/paths/steelseries-arctis-output-chat-common.conf
/usr/share/alsa-card-profile/mixer/paths/steelseries-arctis-output-game-common.conf
/usr/share/alsa-card-profile/mixer/paths/usb-gaming-headset-input.conf
/usr/share/alsa-card-profile/mixer/paths/usb-gaming-headset-output-mono.conf
/usr/share/alsa-card-profile/mixer/paths/usb-gaming-headset-output-stereo.conf
/usr/share/alsa-card-profile/mixer/paths/virtual-surround-7.1.conf
/usr/share/alsa-card-profile/mixer/profile-sets/9999-custom.conf
/usr/share/alsa-card-profile/mixer/profile-sets/analog-only.conf
/usr/share/alsa-card-profile/mixer/profile-sets/asus-xonar-se.conf
/usr/share/alsa-card-profile/mixer/profile-sets/audigy.conf
/usr/share/alsa-card-profile/mixer/profile-sets/cmedia-high-speed-true-hdaudio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/default.conf
/usr/share/alsa-card-profile/mixer/profile-sets/dell-dock-tb16-usb-audio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/force-speaker-and-int-mic.conf
/usr/share/alsa-card-profile/mixer/profile-sets/force-speaker.conf
/usr/share/alsa-card-profile/mixer/profile-sets/hp-tbt-dock-120w-g2.conf
/usr/share/alsa-card-profile/mixer/profile-sets/hp-tbt-dock-audio-module.conf
/usr/share/alsa-card-profile/mixer/profile-sets/kinect-audio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/maudio-fasttrack-pro.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-audio4dj.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-audio8dj.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-komplete-audio6.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-korecontroller.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktor-audio10.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktor-audio2.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktor-audio6.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktorkontrol-s4.conf
/usr/share/alsa-card-profile/mixer/profile-sets/sb-omni-surround-5.1.conf
/usr/share/alsa-card-profile/mixer/profile-sets/sennheiser-gsx.conf
/usr/share/alsa-card-profile/mixer/profile-sets/simple-headphones-mic.conf
/usr/share/alsa-card-profile/mixer/profile-sets/steelseries-arctis-common-usb-audio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/texas-instruments-pcm2902.conf
/usr/share/alsa-card-profile/mixer/profile-sets/usb-gaming-headset.conf
/usr/share/alsa/alsa.conf.d/50-pipewire.conf
/usr/share/alsa/alsa.conf.d/99-pipewire-default.conf
/usr/share/pipewire/client-rt.conf
/usr/share/pipewire/client-rt.conf.avail/20-upmix.conf
/usr/share/pipewire/client.conf
/usr/share/pipewire/client.conf.avail/20-upmix.conf
/usr/share/pipewire/filter-chain.conf
/usr/share/pipewire/filter-chain/demonic.conf
/usr/share/pipewire/filter-chain/sink-dolby-surround.conf
/usr/share/pipewire/filter-chain/sink-eq6.conf
/usr/share/pipewire/filter-chain/sink-make-LFE.conf
/usr/share/pipewire/filter-chain/sink-matrix-spatialiser.conf
/usr/share/pipewire/filter-chain/sink-mix-FL-FR.conf
/usr/share/pipewire/filter-chain/sink-virtual-surround-5.1-kemar.conf
/usr/share/pipewire/filter-chain/sink-virtual-surround-7.1-hesuvi.conf
/usr/share/pipewire/filter-chain/source-duplicate-FL.conf
/usr/share/pipewire/filter-chain/source-rnnoise.conf
/usr/share/pipewire/jack.conf
/usr/share/pipewire/minimal.conf
/usr/share/pipewire/pipewire-aes67.conf
/usr/share/pipewire/pipewire-avb.conf
/usr/share/pipewire/pipewire-pulse.conf
/usr/share/pipewire/pipewire-pulse.conf.avail/20-upmix.conf
/usr/share/pipewire/pipewire.conf
/usr/share/pipewire/pipewire.conf.avail/10-rates.conf
/usr/share/pipewire/pipewire.conf.avail/20-upmix.conf
/usr/share/spa-0.2/bluez5/bluez-hardware.conf

%files dev
%defattr(-,root,root,-)
/usr/include/pipewire-0.3/pipewire/array.h
/usr/include/pipewire-0.3/pipewire/buffers.h
/usr/include/pipewire-0.3/pipewire/client.h
/usr/include/pipewire-0.3/pipewire/conf.h
/usr/include/pipewire-0.3/pipewire/context.h
/usr/include/pipewire-0.3/pipewire/control.h
/usr/include/pipewire-0.3/pipewire/core.h
/usr/include/pipewire-0.3/pipewire/data-loop.h
/usr/include/pipewire-0.3/pipewire/device.h
/usr/include/pipewire-0.3/pipewire/extensions/client-node.h
/usr/include/pipewire-0.3/pipewire/extensions/metadata.h
/usr/include/pipewire-0.3/pipewire/extensions/profiler.h
/usr/include/pipewire-0.3/pipewire/extensions/protocol-native.h
/usr/include/pipewire-0.3/pipewire/extensions/security-context.h
/usr/include/pipewire-0.3/pipewire/extensions/session-manager.h
/usr/include/pipewire-0.3/pipewire/extensions/session-manager/impl-interfaces.h
/usr/include/pipewire-0.3/pipewire/extensions/session-manager/interfaces.h
/usr/include/pipewire-0.3/pipewire/extensions/session-manager/introspect-funcs.h
/usr/include/pipewire-0.3/pipewire/extensions/session-manager/introspect.h
/usr/include/pipewire-0.3/pipewire/extensions/session-manager/keys.h
/usr/include/pipewire-0.3/pipewire/factory.h
/usr/include/pipewire-0.3/pipewire/filter.h
/usr/include/pipewire-0.3/pipewire/global.h
/usr/include/pipewire-0.3/pipewire/i18n.h
/usr/include/pipewire-0.3/pipewire/impl-client.h
/usr/include/pipewire-0.3/pipewire/impl-core.h
/usr/include/pipewire-0.3/pipewire/impl-device.h
/usr/include/pipewire-0.3/pipewire/impl-factory.h
/usr/include/pipewire-0.3/pipewire/impl-link.h
/usr/include/pipewire-0.3/pipewire/impl-metadata.h
/usr/include/pipewire-0.3/pipewire/impl-module.h
/usr/include/pipewire-0.3/pipewire/impl-node.h
/usr/include/pipewire-0.3/pipewire/impl-port.h
/usr/include/pipewire-0.3/pipewire/impl.h
/usr/include/pipewire-0.3/pipewire/keys.h
/usr/include/pipewire-0.3/pipewire/link.h
/usr/include/pipewire-0.3/pipewire/log.h
/usr/include/pipewire-0.3/pipewire/loop.h
/usr/include/pipewire-0.3/pipewire/main-loop.h
/usr/include/pipewire-0.3/pipewire/map.h
/usr/include/pipewire-0.3/pipewire/mem.h
/usr/include/pipewire-0.3/pipewire/module.h
/usr/include/pipewire-0.3/pipewire/node.h
/usr/include/pipewire-0.3/pipewire/permission.h
/usr/include/pipewire-0.3/pipewire/pipewire.h
/usr/include/pipewire-0.3/pipewire/port.h
/usr/include/pipewire-0.3/pipewire/properties.h
/usr/include/pipewire-0.3/pipewire/protocol.h
/usr/include/pipewire-0.3/pipewire/proxy.h
/usr/include/pipewire-0.3/pipewire/resource.h
/usr/include/pipewire-0.3/pipewire/stream.h
/usr/include/pipewire-0.3/pipewire/thread-loop.h
/usr/include/pipewire-0.3/pipewire/thread.h
/usr/include/pipewire-0.3/pipewire/type.h
/usr/include/pipewire-0.3/pipewire/utils.h
/usr/include/pipewire-0.3/pipewire/version.h
/usr/include/pipewire-0.3/pipewire/work-queue.h
/usr/include/spa-0.2/spa/buffer/alloc.h
/usr/include/spa-0.2/spa/buffer/buffer.h
/usr/include/spa-0.2/spa/buffer/meta.h
/usr/include/spa-0.2/spa/buffer/type-info.h
/usr/include/spa-0.2/spa/control/control.h
/usr/include/spa-0.2/spa/control/type-info.h
/usr/include/spa-0.2/spa/debug/buffer.h
/usr/include/spa-0.2/spa/debug/context.h
/usr/include/spa-0.2/spa/debug/dict.h
/usr/include/spa-0.2/spa/debug/file.h
/usr/include/spa-0.2/spa/debug/format.h
/usr/include/spa-0.2/spa/debug/log.h
/usr/include/spa-0.2/spa/debug/mem.h
/usr/include/spa-0.2/spa/debug/node.h
/usr/include/spa-0.2/spa/debug/pod.h
/usr/include/spa-0.2/spa/debug/types.h
/usr/include/spa-0.2/spa/graph/graph.h
/usr/include/spa-0.2/spa/interfaces/audio/aec.h
/usr/include/spa-0.2/spa/monitor/device.h
/usr/include/spa-0.2/spa/monitor/event.h
/usr/include/spa-0.2/spa/monitor/type-info.h
/usr/include/spa-0.2/spa/monitor/utils.h
/usr/include/spa-0.2/spa/node/command.h
/usr/include/spa-0.2/spa/node/event.h
/usr/include/spa-0.2/spa/node/io.h
/usr/include/spa-0.2/spa/node/keys.h
/usr/include/spa-0.2/spa/node/node.h
/usr/include/spa-0.2/spa/node/type-info.h
/usr/include/spa-0.2/spa/node/utils.h
/usr/include/spa-0.2/spa/param/audio/aac-types.h
/usr/include/spa-0.2/spa/param/audio/aac-utils.h
/usr/include/spa-0.2/spa/param/audio/aac.h
/usr/include/spa-0.2/spa/param/audio/alac-utils.h
/usr/include/spa-0.2/spa/param/audio/alac.h
/usr/include/spa-0.2/spa/param/audio/amr-types.h
/usr/include/spa-0.2/spa/param/audio/amr-utils.h
/usr/include/spa-0.2/spa/param/audio/amr.h
/usr/include/spa-0.2/spa/param/audio/ape-utils.h
/usr/include/spa-0.2/spa/param/audio/ape.h
/usr/include/spa-0.2/spa/param/audio/compressed.h
/usr/include/spa-0.2/spa/param/audio/dsd-utils.h
/usr/include/spa-0.2/spa/param/audio/dsd.h
/usr/include/spa-0.2/spa/param/audio/dsp-utils.h
/usr/include/spa-0.2/spa/param/audio/dsp.h
/usr/include/spa-0.2/spa/param/audio/flac-utils.h
/usr/include/spa-0.2/spa/param/audio/flac.h
/usr/include/spa-0.2/spa/param/audio/format-utils.h
/usr/include/spa-0.2/spa/param/audio/format.h
/usr/include/spa-0.2/spa/param/audio/iec958-types.h
/usr/include/spa-0.2/spa/param/audio/iec958-utils.h
/usr/include/spa-0.2/spa/param/audio/iec958.h
/usr/include/spa-0.2/spa/param/audio/layout.h
/usr/include/spa-0.2/spa/param/audio/mp3-types.h
/usr/include/spa-0.2/spa/param/audio/mp3-utils.h
/usr/include/spa-0.2/spa/param/audio/mp3.h
/usr/include/spa-0.2/spa/param/audio/opus.h
/usr/include/spa-0.2/spa/param/audio/ra-utils.h
/usr/include/spa-0.2/spa/param/audio/ra.h
/usr/include/spa-0.2/spa/param/audio/raw-types.h
/usr/include/spa-0.2/spa/param/audio/raw-utils.h
/usr/include/spa-0.2/spa/param/audio/raw.h
/usr/include/spa-0.2/spa/param/audio/type-info.h
/usr/include/spa-0.2/spa/param/audio/vorbis-utils.h
/usr/include/spa-0.2/spa/param/audio/vorbis.h
/usr/include/spa-0.2/spa/param/audio/wma-types.h
/usr/include/spa-0.2/spa/param/audio/wma-utils.h
/usr/include/spa-0.2/spa/param/audio/wma.h
/usr/include/spa-0.2/spa/param/bluetooth/audio.h
/usr/include/spa-0.2/spa/param/bluetooth/type-info.h
/usr/include/spa-0.2/spa/param/buffers-types.h
/usr/include/spa-0.2/spa/param/buffers.h
/usr/include/spa-0.2/spa/param/format-types.h
/usr/include/spa-0.2/spa/param/format-utils.h
/usr/include/spa-0.2/spa/param/format.h
/usr/include/spa-0.2/spa/param/latency-types.h
/usr/include/spa-0.2/spa/param/latency-utils.h
/usr/include/spa-0.2/spa/param/latency.h
/usr/include/spa-0.2/spa/param/param-types.h
/usr/include/spa-0.2/spa/param/param.h
/usr/include/spa-0.2/spa/param/port-config-types.h
/usr/include/spa-0.2/spa/param/port-config.h
/usr/include/spa-0.2/spa/param/profile-types.h
/usr/include/spa-0.2/spa/param/profile.h
/usr/include/spa-0.2/spa/param/profiler-types.h
/usr/include/spa-0.2/spa/param/profiler.h
/usr/include/spa-0.2/spa/param/props-types.h
/usr/include/spa-0.2/spa/param/props.h
/usr/include/spa-0.2/spa/param/route-types.h
/usr/include/spa-0.2/spa/param/route.h
/usr/include/spa-0.2/spa/param/tag-types.h
/usr/include/spa-0.2/spa/param/tag-utils.h
/usr/include/spa-0.2/spa/param/tag.h
/usr/include/spa-0.2/spa/param/type-info.h
/usr/include/spa-0.2/spa/param/video/chroma.h
/usr/include/spa-0.2/spa/param/video/color.h
/usr/include/spa-0.2/spa/param/video/dsp-utils.h
/usr/include/spa-0.2/spa/param/video/dsp.h
/usr/include/spa-0.2/spa/param/video/encoded.h
/usr/include/spa-0.2/spa/param/video/format-utils.h
/usr/include/spa-0.2/spa/param/video/format.h
/usr/include/spa-0.2/spa/param/video/h264-utils.h
/usr/include/spa-0.2/spa/param/video/h264.h
/usr/include/spa-0.2/spa/param/video/mjpg-utils.h
/usr/include/spa-0.2/spa/param/video/mjpg.h
/usr/include/spa-0.2/spa/param/video/multiview.h
/usr/include/spa-0.2/spa/param/video/raw-types.h
/usr/include/spa-0.2/spa/param/video/raw-utils.h
/usr/include/spa-0.2/spa/param/video/raw.h
/usr/include/spa-0.2/spa/param/video/type-info.h
/usr/include/spa-0.2/spa/pod/builder.h
/usr/include/spa-0.2/spa/pod/command.h
/usr/include/spa-0.2/spa/pod/compare.h
/usr/include/spa-0.2/spa/pod/dynamic.h
/usr/include/spa-0.2/spa/pod/event.h
/usr/include/spa-0.2/spa/pod/filter.h
/usr/include/spa-0.2/spa/pod/iter.h
/usr/include/spa-0.2/spa/pod/parser.h
/usr/include/spa-0.2/spa/pod/pod.h
/usr/include/spa-0.2/spa/pod/vararg.h
/usr/include/spa-0.2/spa/support/cpu.h
/usr/include/spa-0.2/spa/support/dbus.h
/usr/include/spa-0.2/spa/support/i18n.h
/usr/include/spa-0.2/spa/support/log-impl.h
/usr/include/spa-0.2/spa/support/log.h
/usr/include/spa-0.2/spa/support/loop.h
/usr/include/spa-0.2/spa/support/plugin-loader.h
/usr/include/spa-0.2/spa/support/plugin.h
/usr/include/spa-0.2/spa/support/system.h
/usr/include/spa-0.2/spa/support/thread.h
/usr/include/spa-0.2/spa/utils/ansi.h
/usr/include/spa-0.2/spa/utils/atomic.h
/usr/include/spa-0.2/spa/utils/cleanup.h
/usr/include/spa-0.2/spa/utils/defs.h
/usr/include/spa-0.2/spa/utils/dict.h
/usr/include/spa-0.2/spa/utils/dll.h
/usr/include/spa-0.2/spa/utils/enum-types.h
/usr/include/spa-0.2/spa/utils/hook.h
/usr/include/spa-0.2/spa/utils/json-pod.h
/usr/include/spa-0.2/spa/utils/json.h
/usr/include/spa-0.2/spa/utils/keys.h
/usr/include/spa-0.2/spa/utils/list.h
/usr/include/spa-0.2/spa/utils/names.h
/usr/include/spa-0.2/spa/utils/ratelimit.h
/usr/include/spa-0.2/spa/utils/result.h
/usr/include/spa-0.2/spa/utils/ringbuffer.h
/usr/include/spa-0.2/spa/utils/string.h
/usr/include/spa-0.2/spa/utils/type-info.h
/usr/include/spa-0.2/spa/utils/type.h
/usr/lib64/libpipewire-0.3.so
/usr/lib64/pkgconfig/libpipewire-0.3.pc
/usr/lib64/pkgconfig/libspa-0.2.pc

%files extras
%defattr(-,root,root,-)
/V3/usr/lib64/gstreamer-1.0/libgstpipewire.so
/usr/lib64/gstreamer-1.0/libgstpipewire.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/alsa-lib/libasound_module_ctl_pipewire.so
/V3/usr/lib64/alsa-lib/libasound_module_pcm_pipewire.so
/V3/usr/lib64/libpipewire-0.3.so.0.1204.0
/V3/usr/lib64/pipewire-0.3/libpipewire-module-access.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-adapter.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-avb.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-client-device.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-client-node.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-combine-stream.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-echo-cancel.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-fallback-sink.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-filter-chain.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-jack-tunnel.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-jackdbus-detect.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-link-factory.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-loopback.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-metadata.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-netjack2-driver.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-netjack2-manager.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-parametric-equalizer.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-pipe-tunnel.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-portal.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-profiler.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-protocol-native.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-protocol-pulse.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-protocol-simple.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-pulse-tunnel.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-raop-sink.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-rt.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-rtkit.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-rtp-sap.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-rtp-sink.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-rtp-source.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-session-manager.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-spa-device-factory.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-spa-device.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-spa-node-factory.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-spa-node.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-vban-recv.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-vban-send.so
/V3/usr/lib64/pipewire-0.3/libpipewire-module-x11-bell.so
/V3/usr/lib64/pipewire-0.3/v4l2/libpw-v4l2.so
/V3/usr/lib64/spa-0.2/aec/libspa-aec-null.so
/V3/usr/lib64/spa-0.2/alsa/libspa-alsa.so
/V3/usr/lib64/spa-0.2/audioconvert/libspa-audioconvert.so
/V3/usr/lib64/spa-0.2/audiomixer/libspa-audiomixer.so
/V3/usr/lib64/spa-0.2/audiotestsrc/libspa-audiotestsrc.so
/V3/usr/lib64/spa-0.2/avb/libspa-avb.so
/V3/usr/lib64/spa-0.2/bluez5/libspa-bluez5.so
/V3/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-faststream.so
/V3/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-opus-g.so
/V3/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-opus.so
/V3/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-sbc.so
/V3/usr/lib64/spa-0.2/control/libspa-control.so
/V3/usr/lib64/spa-0.2/jack/libspa-jack.so
/V3/usr/lib64/spa-0.2/support/libspa-dbus.so
/V3/usr/lib64/spa-0.2/support/libspa-journal.so
/V3/usr/lib64/spa-0.2/support/libspa-support.so
/V3/usr/lib64/spa-0.2/v4l2/libspa-v4l2.so
/V3/usr/lib64/spa-0.2/videoconvert/libspa-videoconvert.so
/V3/usr/lib64/spa-0.2/videotestsrc/libspa-videotestsrc.so
/usr/lib64/alsa-lib/libasound_module_ctl_pipewire.so
/usr/lib64/alsa-lib/libasound_module_pcm_pipewire.so
/usr/lib64/libpipewire-0.3.so.0
/usr/lib64/libpipewire-0.3.so.0.1204.0
/usr/lib64/pipewire-0.3/libpipewire-module-access.so
/usr/lib64/pipewire-0.3/libpipewire-module-adapter.so
/usr/lib64/pipewire-0.3/libpipewire-module-avb.so
/usr/lib64/pipewire-0.3/libpipewire-module-client-device.so
/usr/lib64/pipewire-0.3/libpipewire-module-client-node.so
/usr/lib64/pipewire-0.3/libpipewire-module-combine-stream.so
/usr/lib64/pipewire-0.3/libpipewire-module-echo-cancel.so
/usr/lib64/pipewire-0.3/libpipewire-module-fallback-sink.so
/usr/lib64/pipewire-0.3/libpipewire-module-filter-chain.so
/usr/lib64/pipewire-0.3/libpipewire-module-jack-tunnel.so
/usr/lib64/pipewire-0.3/libpipewire-module-jackdbus-detect.so
/usr/lib64/pipewire-0.3/libpipewire-module-link-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-loopback.so
/usr/lib64/pipewire-0.3/libpipewire-module-metadata.so
/usr/lib64/pipewire-0.3/libpipewire-module-netjack2-driver.so
/usr/lib64/pipewire-0.3/libpipewire-module-netjack2-manager.so
/usr/lib64/pipewire-0.3/libpipewire-module-parametric-equalizer.so
/usr/lib64/pipewire-0.3/libpipewire-module-pipe-tunnel.so
/usr/lib64/pipewire-0.3/libpipewire-module-portal.so
/usr/lib64/pipewire-0.3/libpipewire-module-profiler.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-native.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-pulse.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-simple.so
/usr/lib64/pipewire-0.3/libpipewire-module-pulse-tunnel.so
/usr/lib64/pipewire-0.3/libpipewire-module-raop-sink.so
/usr/lib64/pipewire-0.3/libpipewire-module-rt.so
/usr/lib64/pipewire-0.3/libpipewire-module-rtkit.so
/usr/lib64/pipewire-0.3/libpipewire-module-rtp-sap.so
/usr/lib64/pipewire-0.3/libpipewire-module-rtp-sink.so
/usr/lib64/pipewire-0.3/libpipewire-module-rtp-source.so
/usr/lib64/pipewire-0.3/libpipewire-module-session-manager.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-node-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-node.so
/usr/lib64/pipewire-0.3/libpipewire-module-vban-recv.so
/usr/lib64/pipewire-0.3/libpipewire-module-vban-send.so
/usr/lib64/pipewire-0.3/libpipewire-module-x11-bell.so
/usr/lib64/pipewire-0.3/v4l2/libpw-v4l2.so
/usr/lib64/spa-0.2/aec/libspa-aec-null.so
/usr/lib64/spa-0.2/alsa/libspa-alsa.so
/usr/lib64/spa-0.2/audioconvert/libspa-audioconvert.so
/usr/lib64/spa-0.2/audiomixer/libspa-audiomixer.so
/usr/lib64/spa-0.2/audiotestsrc/libspa-audiotestsrc.so
/usr/lib64/spa-0.2/avb/libspa-avb.so
/usr/lib64/spa-0.2/bluez5/libspa-bluez5.so
/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-faststream.so
/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-opus-g.so
/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-opus.so
/usr/lib64/spa-0.2/bluez5/libspa-codec-bluez5-sbc.so
/usr/lib64/spa-0.2/control/libspa-control.so
/usr/lib64/spa-0.2/jack/libspa-jack.so
/usr/lib64/spa-0.2/support/libspa-dbus.so
/usr/lib64/spa-0.2/support/libspa-journal.so
/usr/lib64/spa-0.2/support/libspa-support.so
/usr/lib64/spa-0.2/v4l2/libspa-v4l2.so
/usr/lib64/spa-0.2/videoconvert/libspa-videoconvert.so
/usr/lib64/spa-0.2/videotestsrc/libspa-videotestsrc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pipewire/13641f6e59f451fcd8b6f92b449b91e4265854a5
/usr/share/package-licenses/pipewire/b20949a01ecd5fc139d843db8a3e3b66b6ab8623

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/filter-chain.service
/usr/lib/systemd/user/pipewire-pulse.service
/usr/lib/systemd/user/pipewire-pulse.socket
/usr/lib/systemd/user/pipewire.service
/usr/lib/systemd/user/pipewire.socket
/usr/lib/systemd/user/sockets.target.wants/pipewire-pulse.socket
/usr/lib/systemd/user/sockets.target.wants/pipewire.socket

%files locales -f pipewire.lang
%defattr(-,root,root,-)

