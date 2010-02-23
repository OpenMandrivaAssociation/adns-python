Summary:	Python bindings for GNU adns library
Name:		adns-python
Version:	1.2.1
Release:	%mkrel 2
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	adns-devel
%py_requires -d
URL:		http://dustman.net/andy/python/adns-python

%description
adns-python is a Python module that interfaces to the adns asynchronous
resolver library.

%prep
%setup -q

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc GPL README
%{_libdir}/python%{pyver}/site-packages/*


