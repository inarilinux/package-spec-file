Name:           python3-adblockparser
Version:        0.7
Release:        1.inari1
Summary:        Python parser for Adblock Plus filters. 

License:        MIT
URL:            https://github.com/scrapinghub/adblockparser
Source0:        https://github.com/scrapinghub/adblockparser/archive/refs/tags/0.7.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel pyproject-rpm-macros

%description
adblockparser is a package for working with Adblock Plus filter rules. It can parse Adblock Plus filters and match URLs against them.

%prep
%autosetup -p1 -n adblockparser-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files adblockparser

%files -n %{name} -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license LICENSE.txt

%changelog
* Wed Jan 1 2025 codeoftheghost <0x7ccghost@gmail.com> - 0.7.1-1inari1
- Initial release python3-adblockparser for inari-linux 1 "kogitsune".
