Name:           sqlmap
Version:        1.8
Release:        1.inari1
Summary:        Automatic SQL injection and database takeover tool
Group:          Security/database
License:        GPLv3
URL:            https://sqlmap.org/
Source0:        https://github.com/sqlmapproject/sqlmap/archive/refs/tags/1.8.tar.gz
BuildArch:      noarch
Requires:       python3 python3-requests

%description
sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester, and a broad range of switches including database fingerprinting, over data fetching from the database, accessing the underlying file system, and executing commands on the operating system via out-of-band connections.

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 0775 %{buildroot}%{_datadir}/%{name}
install -m 0755 sqlmap.py %{buildroot}%{_datadir}/%{name}
cp -pr extra %{buildroot}%{_datadir}/%{name}
cp -pr lib %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
cp -pr data %{buildroot}%{_datadir}/%{name}
cp -pr thirdparty %{buildroot}%{_datadir}/%{name}

install -d -m 0755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/sqlmap << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./sqlmap.py "$@"
EOF
chmod +x %{buildroot}%{_bindir}/sqlmap

find %{buildroot}%{_datadir}/%{name} -type f -name "*.py" -exec sed -i 's|/usr/bin/env python$|/usr/bin/python3|' {} +
find %{buildroot}%{_datadir}/%{name} -type f -name "*.sh" -exec sed -i 's|^#!/bin/bash$|#!/usr/bin/bash|' {} +

install -d -m 0755 %{buildroot}%{_sysconfdir}
install -m 0644 sqlmap.conf %{buildroot}%{_sysconfdir}
pushd %{buildroot}%{_datadir}/%{name}
ln -s ../../..%{_sysconfdir}/sqlmap.conf .

%files
%license LICENSE
%doc doc/*
%doc README.md
%{_datadir}/%{name}
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Tue Dec 18 2024 Ghost <0x7ccghost@gmail.com> - 1.8-1.inari1
- Initial release sqlmap for inari-linux 1 "kogitsune"
