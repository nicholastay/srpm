%global _missing_build_ids_terminate_build 0
# Not sure what build IDs are, but fasm's exes don't have these.
%undefine _debugsource_packages
# No debug source for this.

Name:     fasm
Version:  1.73.29
Release:  0%{?dist}
Summary:  flat assembler - open source assembly language compiler
Packager: Nicholas Tay <nick@windblume.net>

License: BSD-2-Clause
URL:     https://flatassembler.net
Source0: %{url}/%{name}-%{version}.tgz

%description
The flat assembler (abbreviated to fasm, intentionally stylized with lowercase letters) is a fast assembler running in a variety of operating systems, in continued development since 1999. It was designed primarily for the assembly of x86 instructions and it supports x86 and x86-64 instructions sets with extensions like MMX, 3DNow!, SSE up to SSE4, AVX, AVX2, XOP, and AVX-512. It can produce output in plain binary, MZ, PE, COFF or ELF format. It includes a powerful but simple macroinstruction system and does multiple passes to optimize the size of instruction codes. The flat assembler is self-hosting and the complete source code is included.


%prep
%autosetup -n %{name}


%build
./%{name}.x64 ./source/Linux/x64/%{name}.asm


%install
%__install -Dm755 source/Linux/x64/%{name} %{buildroot}%{_bindir}/%{name}


%files
%license license.txt
%{_bindir}/%{name}


%changelog
* Sun Jan 9 2022 Nicholas Tay <nick@windblume.net>
- Initial spec
