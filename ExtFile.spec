%define name      ExtFile
%define longtitle A Zope product to store larges files outside the ZODB
%define version   1.1.3
%define release   %mkrel 5





Name:               %name
Summary:            %longtitle
Version:            %version
Release:            %release
Group:              Development/Python
Requires:           zope python-imaging
License:            GPL
URL:                http://www.zope.org
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir
Buildarch:	noarch

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
