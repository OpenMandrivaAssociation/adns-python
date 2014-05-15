Summary:	Python bindings for GNU adns library
Name:		adns-python
Version:	1.2.1
Release:	3
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRequires:	adns-devel
BuildRequires:  python-devel
URL:		http://dustman.net/andy/python/adns-python

%description
adns-python is a Python module that interfaces to the adns asynchronous
resolver library.

%prep
%setup -q

%build
env CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc GPL README
%{_libdir}/python%{py_ver}/site-packages/*

