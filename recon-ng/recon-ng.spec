Name:           recon-ng
Version:        5.1.2
Release:        1.inari1

Summary:        Open Source Intelligence gathering tool aimed at reducing the time spent harvesting information from open sources. 
License:        GPLv3
URL:            https://github.com/lanmaster53/recon-ng
Source0:        https://github.com/lanmaster53/recon-ng/archive/refs/tags/v5.1.2.tar.gz
BuildArch:      noarch
Requires:       python3-pyyaml python3-dns python3-lxml python3-mechanize python3-requests python3-flask-restx python3-flasgger python3-dicttoxml python3-xlxwriter python3-rq

%description
Recon-ng is a full-featured reconnaissance framework designed with the goal of providing a powerful environment to conduct open source web-based reconnaissance quickly and thoroughly. Recon-ng has a look and feel similar to the Metasploit Framework, reducing the learning curve for leveraging the framework. However, it is quite different. Recon-ng is not intended to compete with existing frameworks, as it is designed exclusively for web-based open source reconnaissance. If you want to exploit, use the Metasploit Framework. If you want to social engineer, use the Social-Engineer Toolkit. If you want to conduct reconnaissance, use Recon-ng!

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -m 0755 recon-cli %{buildroot}%{_datadir}/%{name}
install -m 0755 recon-ng %{buildroot}%{_datadir}/%{name}
install -m 0755 recon-web %{buildroot}%{_datadir}/%{name}
install -m 0755 VERSION %{buildroot}%{_datadir}/%{name}
cp -pr recon %{buildroot}%{_datadir}/%{name}

install -d -m 0755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/recon-ng << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./recon-ng "$@"
EOF

cat > %{buildroot}%{_bindir}/recon-cli << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./recon-cli "$@"
EOF

cat > %{buildroot}%{_bindir}/recon-cli << 'EOF'
#!/usr/bin/bash
cd %{_datadir}/%{name}
./recon-web "$@"
EOF

chmod 0755 %{buildroot}%{_bindir}/%{name}

find %{buildroot}%{_datadir}/%{name} -type f -name "*.py" -exec sed -i 's|/usr/bin/env python$|/usr/bin/python3|' {} +

%files
%license LICENSE
%doc README.md
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
* Sun Dec 22 2024 Ghost <0x7ccghost@gmail.com> - 5.1.2-1.inari1
- Initial release sqlmap for inari-linux 1 "kogitsune"