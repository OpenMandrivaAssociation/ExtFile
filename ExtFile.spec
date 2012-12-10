%define name      ExtFile
%define longtitle A Zope product to store larges files outside the ZODB
%define version   1.1.3
%define release   %mkrel 9





Name:               %name
Summary:            %longtitle
Version:            %version
Release:            %release
Group:              Development/Python
Requires:           zope python-imaging
License:            GPL
URL:                http://www.zope.org
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir

Source: %{name}-%{version}.tar.bz2

#----------------------------------------------------------------------
%description
A Zope product to store larges files outside the ZODB

#----------------------------------------------------------------------
%prep

rm -rf $RPM_BUILD_ROOT
%setup -a 0

#----------------------------------------------------------------------
%build

#----------------------------------------------------------------------
%install

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install %{name}-%{version}/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install %{name}-%{version}/*.txt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install %{name}-%{version}/*.dtml $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/www
install %{name}-%{version}/www/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/www

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons
install %{name}-%{version}/icons/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons
install %{name}-%{version}/icons/*.html $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/application
install %{name}-%{version}/icons/application/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/application
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/audio
install %{name}-%{version}/icons/audio/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/audio
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/image
install %{name}-%{version}/icons/image/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/image
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/text
install %{name}-%{version}/icons/text/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/text
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/video
install %{name}-%{version}/icons/video/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons/video

%clean
rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------------------
%files
%defattr(-,root,root,0755)
%doc README.txt CHANGES.txt LICENSE.txt version.txt

%{_libdir}/zope/lib/python/Products/%{name}/

#----------------------------------------------------------------------


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-9mdv2011.0
+ Revision: 616413
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-8mdv2010.0
+ Revision: 428660
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-7mdv2009.0
+ Revision: 266089
- rebuild early 2009.0 package (before pixel changes)

* Mon May 12 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.1.3-6mdv2009.0
+ Revision: 206511
- Should not be noarch ed

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1.3-5mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ExtFile


* Mon Jun 19 2006 Lenny Cartier <lenny@mandriva.com> 1.1.3-5mdv2007.0
- rebuild

* Fri May 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.3-4mdk
- Rebuild

* Wed Sep 05 2003 Sebastien Robin <seb@nexedi.com> 1.1.3-3mdk
- Update spec in order to follows Mandrake Rules

* Wed Apr 25 2003 Sebastien Robin <seb@nexedi.com> 1.1.3-2nxd
- Clean the spec file

* Mon Feb 3 2003 Jean-Paul Smets <jp@nexedi.com> 1.1.3-1nxd
- Initial release
