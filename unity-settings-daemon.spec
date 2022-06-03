%define _disable_ld_no_undefined 1

%define _version 15.04.1+21.10.20210715
Name:           unity-settings-daemon
Version:        15.04.1
Release:        1
Summary:        Unity session settings daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://launchpad.net/unity-settings-daemon
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
#Source1:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE 0001-Remove-accountsservice-dependency.patch -- Remove accountsservice dependency.
Patch0:         0001-Remove-accountsservice-dependency.patch
# PATCH-FIX-UPSTREAM 0002-fix-warnings.patch -- Fix some warnings.
#Patch1:         0002-fix-warnings.patch

BuildRequires:  pkgconfig(packagekit-glib2)
#BuildRequires:  accountsservice
#BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fcitx
BuildRequires:  fcitx-gtk
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xkeyboard-config
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(fcitx)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gsettings-unity-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-wacom)
BuildRequires:  pkgconfig(xtst)

%description
This package contains the daemon which is responsible for setting
the various parameters of a Unity 7 session and the applications
that run under it.

%lang_package

%package devel
Summary:        Development headers for Unity Settings Daemon
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains the daemon which is responsible for setting
the various parameters of a Unity 7 session and the applications
that run under it.

This package provides development headers for
unity-settings-daemon.

%prep
%autosetup -c -p1

%build
#export CC=gcc
#export CXX=g++
NOCONFIGURE=1 ./autogen.sh
%configure \
  --libexecdir=%{_libexecdir}/%{name} \
  --disable-static \
  --enable-ibus
%make_build

%install
%make_install

mv %{buildroot}%{_prefix}/lib/udev/rules.d/61-{gnome,unity}-settings-daemon-rfkill.rules

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING*
%doc AUTHORS MAINTAINERS
%{_sysconfdir}/xdg/autostart/unity-fallback-mount-helper.desktop
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_libdir}/lib%{name}.so.*
%{_libdir}/%{name}*/
%{_libexecdir}/%{name}/
%{_datadir}/%{name}*/
%{_prefix}/lib/udev/rules.d/61-%{name}-rfkill.rules
%{_datadir}/polkit-1/actions/com.ubuntu.%{name}.plugins.*.policy
%{_datadir}/icons/hicolor/*/apps/usd-xrandr.*
%{_datadir}/glib-2.0/schemas/com.canonical.unity.settings-daemon.*.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files devel
%{_includedir}/%{name}-1.0/
%{_libdir}/libunity-settings-daemon.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/pkgconfig/%{name}.pc
