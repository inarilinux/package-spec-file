Name:           amass
Version:        4.2.0
Release:        3.inari1

Summary:        In-depth attack surface mapping and asset discovery
License:        ASL 2.0
URL:            https://github.com/owasp-amass/amass
Source0:        https://github.com/owasp-amass/amass/releases/download/v4.2.0/amass_Linux_amd64.zip
BuildRequires:  unzip

%description
The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.

%prep
%autosetup -c -T
unzip %{Source0}

%install
install -d -m 0755 %{buildroot}%{_bindir}/%{name}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat Dec 21 2024 Ghost <0x7ccghost@gmail.com> - 4.2.0-3.inari1
- Change source to pre-build binary

* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 4.2.0-2.inari1
- Removing all tools group. Replace by meta-package

* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 4.2.0-1.inari1
- Initial release amass for inari-linux 1 "kogitsune"
