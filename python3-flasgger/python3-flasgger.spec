Name:           python3-flasgger
Version:        0.9.7.1
Release:        1.inari1
Summary:        Extract swagger specs from your flask project

License:        MIT
URL:            https://github.com/flasgger/flasgger/
Source0:        https://github.com/flasgger/flasgger/archive/refs/tags/v0.9.7.1.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel pyproject-rpm-macros

%description
Flasgger is a Flask extension to extract OpenAPI-Specification from all Flask views registered in your API. Flasgger also comes with SwaggerUI embedded so you can access http://localhost:5000/apidocs and visualize and interact with your API resources. Flasgger also provides validation of the incoming data, using the same specification it can validates if the data received as a POST, PUT, PATCH is valid against the schema defined using YAML, Python dictionaries or Marshmallow Schemas. Flasgger can work with simple function views or MethodViews using docstring as specification, or using @swag_from decorator to get specification from YAML or dict and also provides SwaggerView which can use Marshmallow Schemas as specification.

%prep
%autosetup -p1 -n flasgger-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%files -n %{name} -f %{pyproject_files}
%doc README.md HISTORY
%license LICENSE

%changelog
* Sat Dec 21 2024 codeoftheghost <0x7ccghost@gmail.com> - 0.9.7.1-1
- Initial release python3-flasgger for inari-linux 1 "kogitsune".
