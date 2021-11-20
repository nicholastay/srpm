%define git_commit db7200f689b97d564b59aba55c5a68cab2e45949
%define git_short %(c=%{git_commit}; echo ${c:0:7})

%define source_name dragon
%define real_name dragon-drop

Name:     dragon-drop-git
Version:  1.1.g%{git_short}
Release:  0%{?dist}
Summary:  simple drag-and-drop source/sink for X or Wayland
Packager: Nicholas Tay <nick@windblume.net>

License: GPLv3
URL:     https://github.com/mwh/dragon
Source0: %{URL}/archive/%{git_commit}.tar.gz
#Source0: %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gtk3-devel

Requires: gtk3

Conflicts: dragon-drop

%description
dragon - simple drag-and-drop source/sink for X or Wayland

Many programs, particularly web applications, expect files to be dragged
into them now. If you don't habitually use a file manager that is a
problem. dragon is a lightweight drag-and-drop source for X where you
can run:
  dragon file.tar.gz
to get a window with just that file in it, ready to be dragged where you
need it.


%define debug_package %{nil}
%prep
%setup -n %{source_name}-%{git_commit}


%build
%make_build NAME=%{real_name} PREFIX=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
%make_install NAME=%{real_name} PREFIX=%{_prefix}


%files
%license LICENCE
%{_bindir}/%{real_name}
%{_mandir}/man1/%{real_name}.1.gz



%changelog
* Sat Nov 20 2021 Nicholas Tay <nick@windblume.net>
- Initial spec
