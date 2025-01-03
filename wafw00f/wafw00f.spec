Name:           wafw00f
Version:        2.3.1
Release:        1.inari1
Summary:        Tool to identifies and fingerprints Web Application Firewall (WAF)
Group:          Security/information-gathering
License:        BSD
URL:            https://github.com/EnableSecurity/wafw00f.git
Source0:        https://github.com/EnableSecurity/wafw00f/archive/refs/tags/v2.3.1.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel python3-setuptools

%description
WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

%prep
%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' {wafw00f/*.py,wafw00f/*/*.py}

%build
%py3_build

%install
%py3_install

%files
%doc CREDITS.txt README.md CODE_OF_CONDUCT.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Wed Jan 01 2025 Ghost <0x7ccghost@gmail.com> - 2.3.1-1.inari1
- Update upstream version

* Fri Dec 20 2024 Ghost <0x7ccghost@gmail.com> - 2.2.0-1.inari1
- Initial package wafw00f 2.2.0 for Inari Linux