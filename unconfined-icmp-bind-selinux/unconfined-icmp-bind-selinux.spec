%global modulename unconfined-icmp-bind
%global selinuxtype targeted

Name:    unconfined-icmp-bind-selinux
Version: 1.0
Release: 1
Summary: SELinux policy to allow ICMP socket bind in unconfined_t

License: BSD-2-Clause
Source0: %{modulename}.te

BuildArch:      noarch
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel

%description
Simple SELinux policy to allow name_bind/node_bind for ICMP sockets
in unconfined_t contexts. Probably useful for something like OpenNMS
or some games.

# (Reading: https://fedoraproject.org/wiki/SELinux/IndependentPolicy)

%build
mkdir selinux
cp -p %{SOURCE0} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp

%install
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%files
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%changelog
* Mon Jan 15 2023 Nicholas Tay <nick@windblume.net>
- Initial rpm
