Name:           python3-exif-legacy
Version:        2.3.2
Release:        1.inari1
Summary:        Easy to use Python module to extract Exif metadata from digital image files.

License:        BSD-3-Clause
URL:            https://github.com/ianare/exif-py
Source0:        https://github.com/ianare/exif-py/archive/refs/tags/2.3.2.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel pyproject-rpm-macros

%description
Easy to use Python module to extract Exif metadata from digital image files. Supported formats: TIFF, JPEG, PNG, Webp, HEIC

%prep
%autosetup -p1 -n exif-py-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files exifread

%files -n %{name} -f %{pyproject_files}
%{_bindir}/EXIF.py
%doc README.rst ChangeLog.rst CONTRIBUTING.rst
%license LICENSE.txt

%changelog
* Wed Jan 1 2025 codeoftheghost <0x7ccghost@gmail.com> - 2.3.2-1inari1
- Initial release python3-exif-legacy for inari-linux 1 "kogitsune".
