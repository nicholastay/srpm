Name:     ueberzug
Version:  18.1.9
Release:  0%{?dist}
Summary:  Überzug is a command line util which allows to draw images on terminals by using child windows.
Packager: Nicholas Tay <nick@windblume.net>

License: GPLv3
URL:     https://github.com/seebye/ueberzug
Source0: %{URL}/archive/refs/tags/%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: python3-pillow
BuildRequires: python3-docopt
BuildRequires: python3-attrs
BuildRequires: python3-xlib

Requires: python3
Requires: libX11
Requires: libXext
Requires: python3-pillow
Requires: python3-docopt
Requires: python3-attrs
Requires: python3-xlib

%description
Überzug is a command line util which allows to draw images on terminals by using child windows.

Advantages to w3mimgdisplay:

- no race conditions as a new window is created to display images
- expose events will be processed,
- so images will be redrawn on switch workspaces
- tmux support (excluding multi pane windows)
- terminals without the WINDOWID environment variable are supported
- chars are used as position - and size unit
- no memory leak (/ unlimited cache)


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ueberzug


%check
%pyproject_check_import


%files -n ueberzug -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitearch}/Xshm%{python3_ext_suffix}


%changelog
* Sat Nov 20 2021 Nicholas Tay <nick@windblume.net>
- Initial spec
