%define develname %mklibname -d bt
Name: libbt
Version: 1.06
Release: 8
Summary: C-language Impementation of the BitTorrent core protocols
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPL+ and LGPL+
Group: Development/C++
URL: http://libbt.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/libbt/libbt-%{version}.tar.gz
Patch0: libbt-1.06-header.patch
Patch1: libbt-1.06-fix-linking.patch
BuildRequires: curl-devel

%description
LibBT is a C reimplementation of the BitTorrent core protocols.  Our goal for
the project is to develop a low overhead library version of the protocols so
that BitTorrent transfers can easily be built in to any existing application.

The sample applications included with LibBT currently run in between 2Mb and
3.5Mb of memory (RSS), depending on the number of peers that are attached.

%package utils
Summary: C-language Impementation of the BitTorrent core protocols
Group: Networking/File transfer

%description utils
LibBT is a C reimplementation of the BitTorrent core protocols.  Our goal for
the project is to develop a low overhead library version of the protocols so
that BitTorrent transfers can easily be built in to any existing application.

This contains the sample applications from LibBT, that currently run
in between 2Mb and 3.5Mb of memory (RSS), depending on the number of
peers that are attached.

%package -n %develname
Summary: C-language Impementation of the BitTorrent core protocols
Group: Development/C
%if %_lib != lib
Obsoletes: libbt-devel
%endif

%description -n %develname
LibBT is a C reimplementation of the BitTorrent core protocols.  Our goal for
the project is to develop a low overhead library version of the protocols so
that BitTorrent transfers can easily be built in to any existing application.

The sample applications included with LibBT currently run in between 2Mb and
3.5Mb of memory (RSS), depending on the number of peers that are attached.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
%{__install} -Dd -m 0755                     \
    $RPM_BUILD_ROOT%{_bindir}/               \
    $RPM_BUILD_ROOT%{_libdir}/               \
    $RPM_BUILD_ROOT%{_includedir}/%{name}    \
    $RPM_BUILD_ROOT%{_mandir}/man1/



%{__install} -m 0755 src/{btcheck,btlist,btget} \
    $RPM_BUILD_ROOT%{_bindir}/

%{__install} -m 0644 src/%{name}.a \
    $RPM_BUILD_ROOT%{_libdir}/

%{__install} -m 0644 man/*.1        \
    $RPM_BUILD_ROOT%{_mandir}/man1/

%{__install} -m 0644                                          \
        include/{benc.h,bitset.h,bterror.h,btmessage.h,bts.h} \
        include/{context.h,peer.h,random.h,segmenter.h}       \
        include/{strbuf.h,stream.h,types.h,util.h}            \
    $RPM_BUILD_ROOT%{_includedir}/%{name}

mv %buildroot%_bindir/btcheck %buildroot%_bindir/bt-check
mv %buildroot%_mandir/man1/btcheck.1 %buildroot%_mandir/man1/bt-check.1

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files utils
%defattr(-,root,root)
%doc CHANGELOG CREDITS README errorlist.txt
%{_bindir}/bt*
%{_mandir}/man1/bt*

%files -n %develname
%defattr(-,root,root)
%doc docs/*.txt
%{_libdir}/%{name}.a
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*




%changelog
* Tue Dec 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.06-7mdv2012.0
+ Revision: 738262
- fix linking
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.06-6mdv2011.0
+ Revision: 609734
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.06-5mdv2010.1
+ Revision: 537320
- rebuild

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.06-4mdv2010.0
+ Revision: 455875
- rebuild for new curl SSL backend

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.06-3mdv2010.0
+ Revision: 438517
- rebuild

* Sat Oct 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.06-2mdv2009.1
+ Revision: 291902
- update patch for gcc 4.3
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.06-1mdv2008.1
+ Revision: 96155
- new version
- new devel name


* Fri Jan 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.05-4mdv2007.0
+ Revision: 104423
- Import libbt

* Fri Jan 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.05-4mdv2007.1
- Rebuild

* Fri Jul 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.05-1mdv2007.0
- Rebuild

* Mon Apr 10 2006 Götz Waschk <waschk@mandriva.org> 1.05-2mdk
- rename btcheck as there's a conflict with perl-Text-BibTeX

* Sun Dec 11 2005 Götz Waschk <waschk@mandriva.org> 1.05-1mdk
- build patch
- New release 1.05
- use mkrel

* Thu Apr 28 2005 Götz Waschk <waschk@mandriva.org> 1.04-1mdk
- new version

* Sun Feb 20 2005 Götz Waschk <waschk@linux-mandrake.com> 1.03-1mdk
- initial mdk package

* Sat Dec 18 2004 - darix@irssi.org
- initial package

