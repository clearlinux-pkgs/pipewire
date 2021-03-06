#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pipewire
Version  : 0.3.31
Release  : 23
URL      : https://github.com/PipeWire/pipewire/archive/0.3.31/pipewire-0.3.31.tar.gz
Source0  : https://github.com/PipeWire/pipewire/archive/0.3.31/pipewire-0.3.31.tar.gz
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
BuildRequires : SDL2-dev
BuildRequires : buildreq-meson
BuildRequires : libcap-dev
BuildRequires : libusb-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(avahi-client)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(systemd)
BuildRequires : valgrind

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

%description services
services components for the pipewire package.


%package tests
Summary: tests components for the pipewire package.
Group: Default
Requires: pipewire = %{version}-%{release}

%description tests
tests components for the pipewire package.


%prep
%setup -q -n pipewire-0.3.31
cd %{_builddir}/pipewire-0.3.31
pushd ..
cp -a pipewire-0.3.31 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624902899
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dbluez5-backend-ofono=disabled \
-Dinstalled_tests=enabled \
-Dpipewire-jack=disabled \
-Dudevrulesdir="/usr/lib/udev/rules.d" \
-Dvulkan=disabled \
-Dlibcamera=disabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --libdir=lib64/haswell --prefix=/usr --buildtype=plain -Dbluez5-backend-ofono=disabled \
-Dinstalled_tests=enabled \
-Dpipewire-jack=disabled \
-Dudevrulesdir="/usr/lib/udev/rules.d" \
-Dvulkan=disabled \
-Dlibcamera=disabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/pipewire
cp %{_builddir}/pipewire-0.3.31/COPYING %{buildroot}/usr/share/package-licenses/pipewire/13641f6e59f451fcd8b6f92b449b91e4265854a5
cp %{_builddir}/pipewire-0.3.31/LICENSE %{buildroot}/usr/share/package-licenses/pipewire/b20949a01ecd5fc139d843db8a3e3b66b6ab8623
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang pipewire

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pipewire
/usr/bin/pipewire-media-session
/usr/bin/pipewire-pulse
/usr/bin/pw-cat
/usr/bin/pw-cli
/usr/bin/pw-dot
/usr/bin/pw-dump
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
/usr/share/alsa-card-profile/mixer/profile-sets/audigy.conf
/usr/share/alsa-card-profile/mixer/profile-sets/behringer-umc22.conf
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
/usr/share/alsa-card-profile/mixer/profile-sets/usb-gaming-headset.conf
/usr/share/alsa/alsa.conf.d/50-pipewire.conf
/usr/share/alsa/alsa.conf.d/99-pipewire-default.conf
/usr/share/pipewire/client-rt.conf
/usr/share/pipewire/client.conf
/usr/share/pipewire/filter-chain/demonic.conf
/usr/share/pipewire/filter-chain/sink-dolby-surround.conf
/usr/share/pipewire/filter-chain/sink-eq6.conf
/usr/share/pipewire/filter-chain/sink-matrix-spatialiser.conf
/usr/share/pipewire/filter-chain/source-rnnoise.conf
/usr/share/pipewire/jack.conf
/usr/share/pipewire/media-session.d/alsa-monitor.conf
/usr/share/pipewire/media-session.d/bluez-hardware.conf
/usr/share/pipewire/media-session.d/bluez-monitor.conf
/usr/share/pipewire/media-session.d/media-session.conf
/usr/share/pipewire/media-session.d/v4l2-monitor.conf
/usr/share/pipewire/media-session.d/with-jack
/usr/share/pipewire/media-session.d/with-pulseaudio
/usr/share/pipewire/pipewire-pulse.conf
/usr/share/pipewire/pipewire.conf

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
/usr/include/spa-0.2/spa/debug/dict.h
/usr/include/spa-0.2/spa/debug/format.h
/usr/include/spa-0.2/spa/debug/mem.h
/usr/include/spa-0.2/spa/debug/node.h
/usr/include/spa-0.2/spa/debug/pod.h
/usr/include/spa-0.2/spa/debug/types.h
/usr/include/spa-0.2/spa/graph/graph.h
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
/usr/include/spa-0.2/spa/param/audio/format-utils.h
/usr/include/spa-0.2/spa/param/audio/format.h
/usr/include/spa-0.2/spa/param/audio/layout.h
/usr/include/spa-0.2/spa/param/audio/raw.h
/usr/include/spa-0.2/spa/param/audio/type-info.h
/usr/include/spa-0.2/spa/param/bluetooth/audio.h
/usr/include/spa-0.2/spa/param/bluetooth/type-info.h
/usr/include/spa-0.2/spa/param/format-utils.h
/usr/include/spa-0.2/spa/param/format.h
/usr/include/spa-0.2/spa/param/latency-utils.h
/usr/include/spa-0.2/spa/param/param.h
/usr/include/spa-0.2/spa/param/profiler.h
/usr/include/spa-0.2/spa/param/props.h
/usr/include/spa-0.2/spa/param/type-info.h
/usr/include/spa-0.2/spa/param/video/chroma.h
/usr/include/spa-0.2/spa/param/video/color.h
/usr/include/spa-0.2/spa/param/video/encoded.h
/usr/include/spa-0.2/spa/param/video/format-utils.h
/usr/include/spa-0.2/spa/param/video/format.h
/usr/include/spa-0.2/spa/param/video/multiview.h
/usr/include/spa-0.2/spa/param/video/raw.h
/usr/include/spa-0.2/spa/param/video/type-info.h
/usr/include/spa-0.2/spa/pod/builder.h
/usr/include/spa-0.2/spa/pod/command.h
/usr/include/spa-0.2/spa/pod/compare.h
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
/usr/include/spa-0.2/spa/support/plugin.h
/usr/include/spa-0.2/spa/support/system.h
/usr/include/spa-0.2/spa/utils/ansi.h
/usr/include/spa-0.2/spa/utils/defs.h
/usr/include/spa-0.2/spa/utils/dict.h
/usr/include/spa-0.2/spa/utils/hook.h
/usr/include/spa-0.2/spa/utils/json.h
/usr/include/spa-0.2/spa/utils/keys.h
/usr/include/spa-0.2/spa/utils/list.h
/usr/include/spa-0.2/spa/utils/names.h
/usr/include/spa-0.2/spa/utils/result.h
/usr/include/spa-0.2/spa/utils/ringbuffer.h
/usr/include/spa-0.2/spa/utils/string.h
/usr/include/spa-0.2/spa/utils/type-info.h
/usr/include/spa-0.2/spa/utils/type.h
/usr/lib64/haswell/libpipewire-0.3.so
/usr/lib64/haswell/pkgconfig/libpipewire-0.3.pc
/usr/lib64/haswell/pkgconfig/libspa-0.2.pc
/usr/lib64/libpipewire-0.3.so
/usr/lib64/pkgconfig/libpipewire-0.3.pc
/usr/lib64/pkgconfig/libspa-0.2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/alsa-lib/libasound_module_ctl_pipewire.so
/usr/lib64/alsa-lib/libasound_module_pcm_pipewire.so
/usr/lib64/gstreamer-1.0/libgstpipewire.so
/usr/lib64/haswell/libpipewire-0.3.so.0
/usr/lib64/haswell/libpipewire-0.3.so.0.331.0
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-client-node.so
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-filter-chain.so
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-protocol-native.so
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-protocol-pulse.so
/usr/lib64/haswell/spa-0.2/alsa/libspa-alsa.so
/usr/lib64/haswell/spa-0.2/audioconvert/libspa-audioconvert.so
/usr/lib64/haswell/spa-0.2/audiomixer/libspa-audiomixer.so
/usr/lib64/haswell/spa-0.2/audiotestsrc/libspa-audiotestsrc.so
/usr/lib64/haswell/spa-0.2/bluez5/libspa-bluez5.so
/usr/lib64/haswell/spa-0.2/jack/libspa-jack.so
/usr/lib64/haswell/spa-0.2/support/libspa-support.so
/usr/lib64/haswell/spa-0.2/v4l2/libspa-v4l2.so
/usr/lib64/haswell/spa-0.2/volume/libspa-volume.so
/usr/lib64/libpipewire-0.3.so.0
/usr/lib64/libpipewire-0.3.so.0.331.0
/usr/lib64/pipewire-0.3/libpipewire-module-access.so
/usr/lib64/pipewire-0.3/libpipewire-module-adapter.so
/usr/lib64/pipewire-0.3/libpipewire-module-client-device.so
/usr/lib64/pipewire-0.3/libpipewire-module-client-node.so
/usr/lib64/pipewire-0.3/libpipewire-module-echo-cancel.so
/usr/lib64/pipewire-0.3/libpipewire-module-filter-chain.so
/usr/lib64/pipewire-0.3/libpipewire-module-link-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-loopback.so
/usr/lib64/pipewire-0.3/libpipewire-module-metadata.so
/usr/lib64/pipewire-0.3/libpipewire-module-portal.so
/usr/lib64/pipewire-0.3/libpipewire-module-profiler.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-native.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-pulse.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-simple.so
/usr/lib64/pipewire-0.3/libpipewire-module-pulse-tunnel.so
/usr/lib64/pipewire-0.3/libpipewire-module-rt.so
/usr/lib64/pipewire-0.3/libpipewire-module-rtkit.so
/usr/lib64/pipewire-0.3/libpipewire-module-session-manager.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-node-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-node.so
/usr/lib64/pipewire-0.3/libpipewire-module-zeroconf-discover.so
/usr/lib64/spa-0.2/alsa/libspa-alsa.so
/usr/lib64/spa-0.2/audioconvert/libspa-audioconvert.so
/usr/lib64/spa-0.2/audiomixer/libspa-audiomixer.so
/usr/lib64/spa-0.2/audiotestsrc/libspa-audiotestsrc.so
/usr/lib64/spa-0.2/bluez5/libspa-bluez5.so
/usr/lib64/spa-0.2/control/libspa-control.so
/usr/lib64/spa-0.2/jack/libspa-jack.so
/usr/lib64/spa-0.2/support/libspa-dbus.so
/usr/lib64/spa-0.2/support/libspa-journal.so
/usr/lib64/spa-0.2/support/libspa-support.so
/usr/lib64/spa-0.2/v4l2/libspa-v4l2.so
/usr/lib64/spa-0.2/videoconvert/libspa-videoconvert.so
/usr/lib64/spa-0.2/videotestsrc/libspa-videotestsrc.so
/usr/lib64/spa-0.2/volume/libspa-volume.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pipewire/13641f6e59f451fcd8b6f92b449b91e4265854a5
/usr/share/package-licenses/pipewire/b20949a01ecd5fc139d843db8a3e3b66b6ab8623

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/pipewire-media-session.service
/usr/lib/systemd/user/pipewire-pulse.service
/usr/lib/systemd/user/pipewire-pulse.socket
/usr/lib/systemd/user/pipewire.service
/usr/lib/systemd/user/pipewire.socket

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/benchmark-fmt-ops
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/benchmark-resample
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/test-audioadapter
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/test-audioconvert
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/test-channelmix
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/test-fmt-ops
/usr/libexec/installed-tests/pipewire-0.3/audioconvert/test-resample
/usr/libexec/installed-tests/pipewire-0.3/examples/audio-dsp-filter
/usr/libexec/installed-tests/pipewire-0.3/examples/audio-dsp-src
/usr/libexec/installed-tests/pipewire-0.3/examples/audio-src
/usr/libexec/installed-tests/pipewire-0.3/examples/bluez-session
/usr/libexec/installed-tests/pipewire-0.3/examples/export-sink
/usr/libexec/installed-tests/pipewire-0.3/examples/export-source
/usr/libexec/installed-tests/pipewire-0.3/examples/export-spa
/usr/libexec/installed-tests/pipewire-0.3/examples/export-spa-device
/usr/libexec/installed-tests/pipewire-0.3/examples/local-v4l2
/usr/libexec/installed-tests/pipewire-0.3/examples/spa/adapter-control
/usr/libexec/installed-tests/pipewire-0.3/examples/spa/example-control
/usr/libexec/installed-tests/pipewire-0.3/examples/spa/local-v4l2
/usr/libexec/installed-tests/pipewire-0.3/examples/video-dsp-play
/usr/libexec/installed-tests/pipewire-0.3/examples/video-play
/usr/libexec/installed-tests/pipewire-0.3/examples/video-play-reneg
/usr/libexec/installed-tests/pipewire-0.3/examples/video-src
/usr/libexec/installed-tests/pipewire-0.3/examples/video-src-alloc
/usr/libexec/installed-tests/pipewire-0.3/examples/video-src-reneg
/usr/libexec/installed-tests/pipewire-0.3/pw-test-client
/usr/libexec/installed-tests/pipewire-0.3/pw-test-cpp
/usr/libexec/installed-tests/pipewire-0.3/pw-test-endpoint
/usr/libexec/installed-tests/pipewire-0.3/pw-test-interfaces
/usr/libexec/installed-tests/pipewire-0.3/pw-test-protocol-native
/usr/libexec/installed-tests/pipewire-0.3/pw-test-stream
/usr/libexec/installed-tests/pipewire-0.3/pw-test-utils
/usr/libexec/installed-tests/pipewire-0.3/spa-benchmark-dict
/usr/libexec/installed-tests/pipewire-0.3/spa-benchmark-pod
/usr/libexec/installed-tests/pipewire-0.3/spa-stress-ringbuffer
/usr/share/installed-tests/pipewire-0.3/audioconvert/benchmark-fmt-ops.test
/usr/share/installed-tests/pipewire-0.3/audioconvert/benchmark-resample.test
/usr/share/installed-tests/pipewire-0.3/audioconvert/test-audioadapter.test
/usr/share/installed-tests/pipewire-0.3/audioconvert/test-audioconvert.test
/usr/share/installed-tests/pipewire-0.3/audioconvert/test-channelmix.test
/usr/share/installed-tests/pipewire-0.3/audioconvert/test-fmt-ops.test
/usr/share/installed-tests/pipewire-0.3/audioconvert/test-resample.test
/usr/share/installed-tests/pipewire-0.3/pw-test-client.test
/usr/share/installed-tests/pipewire-0.3/pw-test-cpp.test
/usr/share/installed-tests/pipewire-0.3/pw-test-endpoint.test
/usr/share/installed-tests/pipewire-0.3/pw-test-interfaces.test
/usr/share/installed-tests/pipewire-0.3/pw-test-protocol-native.test
/usr/share/installed-tests/pipewire-0.3/pw-test-stream.test
/usr/share/installed-tests/pipewire-0.3/pw-test-utils.test
/usr/share/installed-tests/pipewire-0.3/spa-benchmark-dict.test
/usr/share/installed-tests/pipewire-0.3/spa-benchmark-pod.test
/usr/share/installed-tests/pipewire-0.3/spa-stress-ringbuffer.test

%files locales -f pipewire.lang
%defattr(-,root,root,-)

