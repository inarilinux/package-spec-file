Name:           dnsenum
Version:        1.3.2
Release:        1.inari1

Summary:        dnsenum is a perl script that enumerates DNS information 
License:        GPLv3
URL:            https://github.com/fwaeytens/dnsenum
Source0:        https://github.com/SparrowOchon/dnsenum2/archive/refs/tags/v1.3.2.tar.gz
BuildArch:      noarch
Requires:       perl perl-String-Random perl-Net-IP perl-Net-DNS perl-Net-Netmask perl-XML-writer


%description
multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_bindir}

cat > %{buildroot}%{_bindir}/dnsrecon << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./dnsrecon.py "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

install -d -m 0775 %{buildroot}%{_datadir}/%{name}
install -m 0755 dnsrecon.py %{buildroot}%{_datadir}/%{name}
cp -pr dnsrecon %{buildroot}%{_datadir}/%{name}
cp -pr tools %{buildroot}%{_datadir}/%{name}
cp -pr tests %{buildroot}%{_datadir}/%{name}

install -d -m 0755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/dnsrecon << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./dnsrecon.py "$@"
EOF
chmod +x %{buildroot}%{_bindir}/dnsrecon

find %{buildroot}%{_datadir}/%{name} -type f -name "*.py" -exec sed -i 's|/usr/bin/env python$|/usr/bin/python3|' {} +

%files
%{_datadir}/%{name}
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 1.3.1-2.inari1
- Removing all tools group. Replace by meta-package

* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 1.3.1-1.inari1
- Initial package dnsrecon 1.3.1 for Inari Linux
