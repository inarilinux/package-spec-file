Name:           dnsrecon
Version:        1.3.1
Release:        2.inari1

Summary:        DNS reconnaissance tool used for performing various DNS enumeration techniques and test, assisting in the directory of potential vulnerabilies in domain configuration
License:        GPLv2
URL:            https://github.com/darkoperator/dnsrecon.git
Source0:        https://github.com/darkoperator/dnsrecon/archive/refs/tags/1.3.1.tar.gz
BuildArch:      noarch
Requires:       python3 python3-requests python3-dns python3-netaddr python3-loguru python3-lxml python3-urllib3 python3-charset-normalizer python3-certifi


%description
dnsrecon is a python-based tool for DNS reconnaissance and security assessments. It automates the collection of DNS records, zone transfers, subdomain enumeration, and cache snooping. Supporting various DNS test, dnsrecon helps reveal configuration vulnerabilities, and facilitates integration with other security tools through flexible output formats.

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
