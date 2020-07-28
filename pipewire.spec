#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pipewire
Version  : 0.3.8
Release  : 11
URL      : https://github.com/PipeWire/pipewire/archive/0.3.8/pipewire-0.3.8.tar.gz
Source0  : https://github.com/PipeWire/pipewire/archive/0.3.8/pipewire-0.3.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: pipewire-bin = %{version}-%{release}
Requires: pipewire-data = %{version}-%{release}
Requires: pipewire-lib = %{version}-%{release}
Requires: pipewire-license = %{version}-%{release}
Requires: pipewire-services = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : glib-dev
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : libsndfile-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(systemd)
BuildRequires : sbc-dev

%description
# PipeWire
[PipeWire](https://pipewire.org) is a server and user space API to
deal with multimedia pipelines. This includes:

%package bin
Summary: bin components for the pipewire package.
Group: Binaries
Requires: pipewire-data = %{version}-%{release}
Requires: pipewire-license = %{version}-%{release}
Requires: pipewire-services = %{version}-%{release}

%description bin
bin components for the pipewire package.


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


%package services
Summary: services components for the pipewire package.
Group: Systemd services

%description services
services components for the pipewire package.


%prep
%setup -q -n pipewire-0.3.8
cd %{_builddir}/pipewire-0.3.8
pushd ..
cp -a pipewire-0.3.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595961205
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvulkan=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --libdir=lib64/haswell --prefix=/usr --buildtype=plain -Dvulkan=false  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/pipewire
cp %{_builddir}/pipewire-0.3.8/COPYING %{buildroot}/usr/share/package-licenses/pipewire/13641f6e59f451fcd8b6f92b449b91e4265854a5
cp %{_builddir}/pipewire-0.3.8/LICENSE %{buildroot}/usr/share/package-licenses/pipewire/1d2540d6544e3a72dd4de79c394aad35e690dc7a
cp %{_builddir}/pipewire-0.3.8/pipewire-pulseaudio/LICENSE %{buildroot}/usr/share/package-licenses/pipewire/731a8eff333b8f7053ab2220511b524c87a75923
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/lib/udev/rules.d/90-pipewire-alsa.rules
/usr/lib64/haswell/pkgconfig/libpipewire-0.3.pc
/usr/lib64/haswell/pkgconfig/libspa-0.2.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/pipewire
/usr/bin/pipewire-media-session
/usr/bin/pw-cat
/usr/bin/pw-cli
/usr/bin/pw-dot
/usr/bin/pw-jack
/usr/bin/pw-metadata
/usr/bin/pw-mididump
/usr/bin/pw-midiplay
/usr/bin/pw-midirecord
/usr/bin/pw-mon
/usr/bin/pw-play
/usr/bin/pw-profiler
/usr/bin/pw-pulse
/usr/bin/pw-record
/usr/bin/spa-inspect
/usr/bin/spa-monitor

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
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-2.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-3.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-4.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-5.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-6.conf
/usr/share/alsa-card-profile/mixer/paths/hdmi-output-7.conf
/usr/share/alsa-card-profile/mixer/paths/iec958-stereo-input.conf
/usr/share/alsa-card-profile/mixer/paths/iec958-stereo-output.conf
/usr/share/alsa-card-profile/mixer/paths/steelseries-arctis-output-chat-common.conf
/usr/share/alsa-card-profile/mixer/paths/steelseries-arctis-output-game-common.conf
/usr/share/alsa-card-profile/mixer/paths/usb-gaming-headset-input.conf
/usr/share/alsa-card-profile/mixer/paths/usb-gaming-headset-output-mono.conf
/usr/share/alsa-card-profile/mixer/paths/usb-gaming-headset-output-stereo.conf
/usr/share/alsa-card-profile/mixer/profile-sets/cmedia-high-speed-true-hdaudio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/default.conf
/usr/share/alsa-card-profile/mixer/profile-sets/dell-dock-tb16-usb-audio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/force-speaker-and-int-mic.conf
/usr/share/alsa-card-profile/mixer/profile-sets/force-speaker.conf
/usr/share/alsa-card-profile/mixer/profile-sets/kinect-audio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/maudio-fasttrack-pro.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-audio4dj.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-audio8dj.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-korecontroller.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktor-audio10.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktor-audio2.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktor-audio6.conf
/usr/share/alsa-card-profile/mixer/profile-sets/native-instruments-traktorkontrol-s4.conf
/usr/share/alsa-card-profile/mixer/profile-sets/sb-omni-surround-5.1.conf
/usr/share/alsa-card-profile/mixer/profile-sets/steelseries-arctis-common-usb-audio.conf
/usr/share/alsa-card-profile/mixer/profile-sets/usb-gaming-headset.conf
/usr/share/alsa/alsa.conf.d/50-pipewire.conf
/usr/share/alsa/alsa.conf.d/99-pipewire-default.conf

%files dev
%defattr(-,root,root,-)
/usr/include/pipewire-0.3/pipewire/array.h
/usr/include/pipewire-0.3/pipewire/buffers.h
/usr/include/pipewire-0.3/pipewire/client.h
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
/usr/include/pipewire-0.3/pipewire/impl-client.h
/usr/include/pipewire-0.3/pipewire/impl-core.h
/usr/include/pipewire-0.3/pipewire/impl-device.h
/usr/include/pipewire-0.3/pipewire/impl-factory.h
/usr/include/pipewire-0.3/pipewire/impl-link.h
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
/usr/include/spa-0.2/spa/param/format-utils.h
/usr/include/spa-0.2/spa/param/format.h
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
/usr/include/spa-0.2/spa/support/log-impl.h
/usr/include/spa-0.2/spa/support/log.h
/usr/include/spa-0.2/spa/support/loop.h
/usr/include/spa-0.2/spa/support/plugin.h
/usr/include/spa-0.2/spa/support/system.h
/usr/include/spa-0.2/spa/utils/defs.h
/usr/include/spa-0.2/spa/utils/dict.h
/usr/include/spa-0.2/spa/utils/hook.h
/usr/include/spa-0.2/spa/utils/keys.h
/usr/include/spa-0.2/spa/utils/list.h
/usr/include/spa-0.2/spa/utils/names.h
/usr/include/spa-0.2/spa/utils/result.h
/usr/include/spa-0.2/spa/utils/ringbuffer.h
/usr/include/spa-0.2/spa/utils/type-info.h
/usr/include/spa-0.2/spa/utils/type.h
/usr/lib64/haswell/libpipewire-0.3.so
/usr/lib64/libpipewire-0.3.so
/usr/lib64/pkgconfig/libpipewire-0.3.pc
/usr/lib64/pkgconfig/libspa-0.2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/alsa-lib/libasound_module_ctl_pipewire.so
/usr/lib64/alsa-lib/libasound_module_pcm_pipewire.so
/usr/lib64/gstreamer-1.0/libgstpipewire.so
/usr/lib64/haswell/libpipewire-0.3.so.0
/usr/lib64/haswell/libpipewire-0.3.so.0.308.0
/usr/lib64/haswell/pipewire-0.3/jack/libjack.so
/usr/lib64/haswell/pipewire-0.3/jack/libjack.so.0
/usr/lib64/haswell/pipewire-0.3/jack/libjack.so.0.308.0
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-client-node.so
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-protocol-native.so
/usr/lib64/haswell/pipewire-0.3/libpipewire-module-session-manager.so
/usr/lib64/haswell/pipewire-0.3/pulse/libpulse.so
/usr/lib64/haswell/pipewire-0.3/pulse/libpulse.so.0
/usr/lib64/haswell/pipewire-0.3/pulse/libpulse.so.0.308.0
/usr/lib64/haswell/spa-0.2/alsa/libspa-alsa.so
/usr/lib64/haswell/spa-0.2/audioconvert/libspa-audioconvert.so
/usr/lib64/haswell/spa-0.2/audiomixer/libspa-audiomixer.so
/usr/lib64/haswell/spa-0.2/bluez5/libspa-bluez5.so
/usr/lib64/haswell/spa-0.2/jack/libspa-jack.so
/usr/lib64/haswell/spa-0.2/v4l2/libspa-v4l2.so
/usr/lib64/libpipewire-0.3.so.0
/usr/lib64/libpipewire-0.3.so.0.308.0
/usr/lib64/pipewire-0.3/jack/libjack.so
/usr/lib64/pipewire-0.3/jack/libjack.so.0
/usr/lib64/pipewire-0.3/jack/libjack.so.0.308.0
/usr/lib64/pipewire-0.3/jack/libjacknet.so
/usr/lib64/pipewire-0.3/jack/libjacknet.so.0
/usr/lib64/pipewire-0.3/jack/libjacknet.so.0.308.0
/usr/lib64/pipewire-0.3/jack/libjackserver.so
/usr/lib64/pipewire-0.3/jack/libjackserver.so.0
/usr/lib64/pipewire-0.3/jack/libjackserver.so.0.308.0
/usr/lib64/pipewire-0.3/libpipewire-module-access.so
/usr/lib64/pipewire-0.3/libpipewire-module-adapter.so
/usr/lib64/pipewire-0.3/libpipewire-module-client-device.so
/usr/lib64/pipewire-0.3/libpipewire-module-client-node.so
/usr/lib64/pipewire-0.3/libpipewire-module-link-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-metadata.so
/usr/lib64/pipewire-0.3/libpipewire-module-portal.so
/usr/lib64/pipewire-0.3/libpipewire-module-profiler.so
/usr/lib64/pipewire-0.3/libpipewire-module-protocol-native.so
/usr/lib64/pipewire-0.3/libpipewire-module-rtkit.so
/usr/lib64/pipewire-0.3/libpipewire-module-session-manager.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-device.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-node-factory.so
/usr/lib64/pipewire-0.3/libpipewire-module-spa-node.so
/usr/lib64/pipewire-0.3/pulse/libpulse-mainloop-glib.so
/usr/lib64/pipewire-0.3/pulse/libpulse-mainloop-glib.so.0
/usr/lib64/pipewire-0.3/pulse/libpulse-mainloop-glib.so.0.308.0
/usr/lib64/pipewire-0.3/pulse/libpulse-simple.so
/usr/lib64/pipewire-0.3/pulse/libpulse-simple.so.0
/usr/lib64/pipewire-0.3/pulse/libpulse-simple.so.0.308.0
/usr/lib64/pipewire-0.3/pulse/libpulse.so
/usr/lib64/pipewire-0.3/pulse/libpulse.so.0
/usr/lib64/pipewire-0.3/pulse/libpulse.so.0.308.0
/usr/lib64/spa-0.2/alsa/libspa-alsa.so
/usr/lib64/spa-0.2/audioconvert/libspa-audioconvert.so
/usr/lib64/spa-0.2/audiomixer/libspa-audiomixer.so
/usr/lib64/spa-0.2/bluez5/libspa-bluez5.so
/usr/lib64/spa-0.2/control/libspa-control.so
/usr/lib64/spa-0.2/jack/libspa-jack.so
/usr/lib64/spa-0.2/support/libspa-dbus.so
/usr/lib64/spa-0.2/support/libspa-support.so
/usr/lib64/spa-0.2/v4l2/libspa-v4l2.so
/usr/lib64/spa-0.2/videoconvert/libspa-videoconvert.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pipewire/13641f6e59f451fcd8b6f92b449b91e4265854a5
/usr/share/package-licenses/pipewire/1d2540d6544e3a72dd4de79c394aad35e690dc7a
/usr/share/package-licenses/pipewire/731a8eff333b8f7053ab2220511b524c87a75923

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/pipewire.service
/usr/lib/systemd/user/pipewire.socket
