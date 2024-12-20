Name:           netdiscover
Version:        0.10
Release:        1.inari1

Summary:        A network address discovering/monitoring tool
License:        GPLv3
URL:            https://netdiscover-scanner/netdiscover.git
Source0:        https://github.com/netdiscover-scanner/netdiscover/archive/refs/tags/0.10.tar.gz
BuildRequires:  gcc libpcap-devel autoconf automake dos2unix hwdata libnet-devel >= 1.1.2

%description
Nerdiscover is an active/passive address reconnaissance tool, mainly developed for those wireless networks without dhcp server, when you are wardriving. It can be also used on hub/switched networks.

Built on top of libnet and libpcap, it can passively detect online hosts, or search for them, by actively sending arp request, it can also be used to inspect your network arp traffic, and find network address using auto scan mode, which will scan for common local networks.

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
