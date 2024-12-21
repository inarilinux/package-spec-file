Name:           meta-dns-analysis
Version:        1.0
Release:        1.inari1

Summary:        Meta-package for dns analysis tools
License:        GPLv3
BuildRequires:  dnf
Requires:       fierce dnsrecon

%description
This meta-package install all collection on dns analysis tools.

%prep
dnf copr enable https://copr.fedorainfracloud.org/coprs/inari-linux/inari-1-kogitsune

%files

%changelog
* Sat Dec 21 2024 Ghost <0x7ccghost@gmail.com> - 1.0-1.inari1
- Initial release meta-dns-analysis for inari-linux 1 "kogitsune"