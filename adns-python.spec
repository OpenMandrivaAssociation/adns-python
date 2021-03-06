Summary:	Python bindings for GNU adns library
Name:		adns-python
Version:	1.2.1
Release:	4
Url:		https://code.google.com/p/adns-python/
Source0:	http://adns-python.googlecode.com/files/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRequires:	adns-devel
BuildRequires:  python2-devel
Requires:  python2


%description
adns-python is a Python module that interfaces to the adns asynchronous
resolver library.

%prep
%setup -q
sed -i 's_#!/usr/bin/env python_#!/usr/bin/env python2_' DNSBL.py
sed -i 's_#!/usr/bin/python_#!/usr/bin/python2_' ADNS.py

%build
env CFLAGS="%{optflags}" python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc GPL README
%{_libdir}/python%{py2_ver}/site-packages/*

