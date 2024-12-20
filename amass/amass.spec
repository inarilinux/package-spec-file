Name:           amass
Version:        4.2.0
Release:        2.inari1

Summary:        In-depth attack surface mapping and asset discovery
License:        ASL 2.0
URL:            https://github.com/owasp-amass/amass
Source0:        https://github.com/owasp-amass/amass/archive/refs/tags/v4.2.0.tar.gz
BuildRequires:  git golang >= 1.19

%description
The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.

%prep
%autosetup -n %{name}-%{version}

%build
go build -o bin/%{name} ./cmd/%{name}

%install
install -d -m 0755 %{buildroot}%{_bindir}/%{name}
install -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc doc/*
%{_bindir}/%{name}

%changelog
* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 4.2.0-2.inari1
- Removing all tools group. Replace by meta-package

* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 4.2.0-1.inari1
- Initial release amass for inari-linux 1 "kogitsune"
