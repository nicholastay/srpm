Name:    jellyfin-media-player
Version: 1.6.1
Release: 1%{?dist}
Summary: Jellyfin Desktop Client

License: GPLv2
URL:     https://github.com/jellyfin/jellyfin-media-player
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz
Source1: https://github.com/iwalton3/jellyfin-web-jmp/releases/download/jwc-10.7.6/dist.zip

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: mpv-libs-devel
BuildRequires: libcec-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
BuildRequires: libXrandr-devel

Requires: mpv
Requires: libcec
Requires: SDL2
Requires: qt5-qtwebengine
Requires: qt5-qtquickcontrols

%description
Unofficial spec file for Jellyfin Media Player. Needs rpmfusion-free.

(This is my first ever RPM package, please excuse any weirdness...)

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_SKIP_RPATH=1
%cmake_build

%install
unzip %{SOURCE1} -d %{_builddir}/%{name}-%{version}/%{_vpath_builddir}
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/jellyfinmediaplayer
%{_datadir}/jellyfinmediaplayer/
%{_datadir}/applications/com.github.iwalton3.jellyfin-media-player.desktop
%{_datadir}/metainfo/com.github.iwalton3.jellyfin-media-player.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.iwalton3.jellyfin-media-player.svg



%changelog

