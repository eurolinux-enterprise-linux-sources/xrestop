Summary: X Resource Monitor
Name: xrestop
Version: 0.4
Release: 14%{?dist}
License: GPLv2+
Group: Development/Tools
URL: http://www.freedesktop.org/Software/xrestop
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: ncurses-devel libXres-devel libXext-devel libX11-devel
BuildRequires: libXau-devel
Patch0: 0001-man-page-Change-dt-to-t.patch
Patch1: 0002-More-man-page-fixes.patch

%description
A utility to monitor application usage of X resources in the X Server, and
display them in a manner similar to 'top'.  This is a very useful utility
for tracking down application X resource usage leaks.

%prep
%setup -q
%patch0 -p1 -b .man-pages0
%patch1 -p1 -b .man-pages1

%build
%configure
make
# SUBDIRS=

%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install
#SUBDIRS=

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/xrestop
%{_mandir}/man1/xrestop.1*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.4-14
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4-13
- Mass rebuild 2013-12-27

* Tue Dec 17 2013 Soren Sandmann <ssp@redhat.com> - 0.4-12
- Man page fixes (#948901)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.4-5
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 0.4-3
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 0.4-2
- Don't install INSTALL

* Tue Feb 13 2007 Adam Jackson <ajax@redhat.com> 0.4-1
- Update to 0.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2-6.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2-6.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.2-6.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec 01 2005 Karsten Hopp <karsten@redhat.de> 0.2-6
- fix build requirements

* Thu Mar  3 2005 Mike A. Harris <mharris@redhat.com> 0.2-5
- Rebuilt with gcc 4 for FC4.

* Thu Oct 14 2004 Mike A. Harris <mharris@redhat.com> 0.2-4
- Added "BuildRequires: xorg-x11-devel, ncurses-devel" (#125029)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 0.2-3
- rebuilt

* Wed Apr 14 2004 Mike A. Harris <mharris@redhat.com> 0.2-2
- Add missing documentation
- Add xrestop-manpage-fix.patch to fix bug (#118038)

* Tue Mar  9 2004 Mike A. Harris <mharris@redhat.com> 0.2-1
- Initial Red Hat RPM package.


