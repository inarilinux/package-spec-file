Name:           dmitry
Version:        1.3
Release:        1.inari1

Summary:        DMitry (Deepmagic Information Gathering Tool) 
License:        GPLv2
URL:            https://github.com/jaygreig86/dmitry
Source0:        https://github.com/inarilinux/dmitry/archive/refs/tags/1.3.tar.gz
BuildRequires:  gcc make autoconf automake

%description
DMitry (Deepmagic Information Gathering Tool) is a UNIX/(GNU)Linux Command Line program coded purely in C with the ability to gather as much information as possible about a host.

DMitry has a base functionality with the ability to add new functions. Basic functionality of DMitry allows for information to be gathered about a target host from a sim- ple whois lookup on the target to UpTime reports and TCP portscans.

The application is considered a tool to assist in informa- tion gathering when information is required quickly by removing the need to enter multiple commands and the timely process of searching through data from multiple sources.

To get straight into DMitry without reading this document, you can initially type "dmitry target", this will perform the majority of functions on the target.

%prep
%setup

%build
if [ ! -f configure ]
then
    ./autogen.sh
    ./configure
fi

%configure
make

%install
%makeinstall
rm -rf $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS TODO README.md
%license %{_defaultdocdir}/%{name}/COPYING
%{_sbindir}/netdiscover
%dir %{_mandir}
%{_mandir}/*

%changelog
* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 0.10.2-inari1
- Removing all tools group. Replace by meta-package

* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 0.10.1-inari1
- Initial release netdiscover for inari-linux 1 "kogitsune"
