Summary:	Python bindings for GNU adns library
Name:		adns-python
Version:	1.2.1
Release:	3
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRequires:	adns-devel
%py_requires -d
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
%defattr(-,root,root)
%doc GPL README
%{_libdir}/python%{py_ver}/site-packages/*




%changelog
* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.1-2mdv2010.1
+ Revision: 510104
- Fix tabs/space
- Fix license

* Wed Jan 20 2010 Frederik Himpe <fhimpe@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 494376
- Remove old patches (srv patch integrated upstream, invalid free patch
  fixed differently upstream)

  + Sandro Cazzaniga <kharec@mandriva.org>
    - set mkrel to 1
    - update to 1.2.1

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-5mdv2010.0
+ Revision: 436626
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 1.1.1-4mdv2009.1
+ Revision: 320370
- rediff srv patch
- rebuild for new python

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 226115
- rebuild
- remove URL from description

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.1.1-2mdv2008.1
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 20 2007 Pascal Terjan <pterjan@mandriva.org> 1.1.1-2mdv2007.1
+ Revision: 146816
- Fix two invalid free

* Wed Dec 06 2006 Jérôme Soyer <saispo@mandriva.org> 1.1.1-1mdv2007.1
+ Revision: 91605
- Add Patch0 from fc
- Rebuild for latest python
- Import adns-python

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 1.0.0-6mdv2007.0
- rebuild

* Wed Aug 24 2005 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 1.0.0-5mdk
- Require python >= 2.5 instead of python = 2.5 (fixes ticket 17152)

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.0.0-4mdk
- Rebuild for new python

* Sat Aug 14 2004 Pascal Terjan <pterjan@mandrake.org> 1.0.0-3mdk
- fix BuildRequires

