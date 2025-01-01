Name:           python3-cherrpy-cors
Version:        1.7.0
Release:        1.inari1
Summary:        CORS support for CherryPy.

License:        MIT
URL:            https://github.com/cherrypy/cherrypy-cors
Source0:        https://github.com/cherrypy/cherrypy-cors/archive/refs/tags/v1.7.0.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel python3-setuptools_scm+toml pyproject-rpm-macros

%description
CORS support for CherryPy

%prep
%autosetup -p1 -n cherrypy-cors-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cherrypy-cors

%files -n %{name} -f %{pyproject_files}
%doc README.rst NEWS.rst
%license LICENSE

%changelog
* Wed Jan 1 2025 codeoftheghost <0x7ccghost@gmail.com> - 1.7.0-1inari1
- Initial release python3-cherrypy-cors for inari-linux 1 "kogitsune".
