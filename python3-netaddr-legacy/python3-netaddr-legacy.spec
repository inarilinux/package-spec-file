Name:           python3-netaddr-legacy
Version:        0.10.1
Release:        1.inari1
Summary:        A network address manipulation library for Python

License:        MIT
URL:            https://github.com/netaddr/netaddr
Source0:        https://github.com/netaddr/netaddr/archive/refs/tags/0.10.1.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel pyproject-rpm-macros

%description
A Python library for representing and manipulating network addresses.

%prep
%autosetup -p1 -n netaddr-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files netaddr

%files -n %{name} -f %{pyproject_files}
%{_bindir}/netaddr
%doc README.rst CHANGELOG AUTHORS THANKS
%license LICENSE COPYRIGHT

%changelog
* Tue Dec 31 2024 codeoftheghost <0x7ccghost@gmail.com> - 0.10.1-1inari1
- Initial release python3-netaddr-legacy for inari-linux 1 "kogitsune".
