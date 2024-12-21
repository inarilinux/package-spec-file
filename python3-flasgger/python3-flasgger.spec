# Created by pyp2rpm-3.3.10
%global pypi_name flasgger
%global pypi_version 0.9.7.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1.inari1
Summary:        Extract swagger specs from your flask project

License:        MIT
URL:            https://github.com/flasgger/flasgger/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flask) >= 0.10
BuildRequires:  python3dist(jsonschema) >= 3.0.1
BuildRequires:  python3dist(mistune)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pyyaml) >= 3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.10

%description
 Flasgger Easy Swagger UI for your Flask API[![Build Status]( [![Code Health](
[![Coverage Status]( [![PyPI]( <a target"_blank" href" alt'Donate with Paypal'
src' /></a>

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flask) >= 0.10
Requires:       python3dist(jsonschema) >= 3.0.1
Requires:       python3dist(mistune)
Requires:       python3dist(packaging)
Requires:       python3dist(pyyaml) >= 3
Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.10
%description -n python3-%{pypi_name}
 Flasgger Easy Swagger UI for your Flask API[![Build Status]( [![Code Health](
[![Coverage Status]( [![PyPI]( <a target"_blank" href" alt'Donate with Paypal'
src' /></a>


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md README.zh.md demo_app/README.md examples/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sat Dec 21 2024 codeoftheghost <0x7ccghost@gmail.com> - 0.9.7.1-1
- Initial release python3-flasgger for inari-linux 1 "kogitsune.
