# fonts-rpm-templates @ /usr/share/rpmdevtools/fedora/spectemplate-fonts-0-simple.spec
Version: 1.8.0
Release: 1%{?dist}
URL:     https://github.com/belluzj/fantasque-sans

BuildArch: noarch

%global foundry           belluzj
%global fontlicense       OFL

%global fontlicenses      LICENSE.txt
%global fontdocs          *.md

%global fontfamily        Fantasque Sans Mono
%global fontsummary       Handwriting-like mono-space font family with coding ligatures

%global fonts             OTF/*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
A programming font, designed with functionality in mind, and with some wibbly-wobbly handwriting-like fuzziness that makes it unassumingly cool. Download or see installation instructions.

Previously known as Cosmic Sans Neue Mono. It appeared that similar names were already in use for other fonts, and that people tended to extend their instinctive hatred of Comic Sans to this very font of mine (which of course can only be loved). Why the previous name? Here is my original explanation:

The name comes from my realization that at some point it looked like the mutant child of Comic Sans and Helvetica Neue. Hopefully it is not the case any more.

Inspirational sources include Inconsolata and Monaco. I have also been using Consolas a lot in my programming life, so it may have some points in common.}

Source0:  %{URL}/releases/download/v%{version}/FantasqueSansMono-Normal.tar.gz
Source10: 62-%{fontpkgname}.conf

%fontpkg

%prep
%setup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sat Nov 20 2021 Nicholas Tay <nick@windblume.net>
- Initial spec
