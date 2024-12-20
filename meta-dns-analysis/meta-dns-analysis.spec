Name:           meta-dns-analysis
Version:        1.0
Release:        1.inari1

Summary:        Meta-package for dns analysis tools
License:        GPLv3

%description
This meta-package install all collection on dns analysis tools.

%package -n meta-dns-analysis
Summary: Collection of dns analysis tools
Requires: fierce dnsrecon

%description -n meta-dns-analysis
Package of multiple dns analysis tools.

%files

%changelog
* Sat Dec 21 2024 Ghost <0x7ccghost@gmail.com> - 1.0-1.inari1
- Initial release meta-dns-analysis for inari-linux 1 "kogitsune"