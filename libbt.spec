%define develname %mklibname -d bt
Name: libbt
Version: 1.06
Release: %mkrel 4
Summary: C-language Impementation of the BitTorrent core protocols
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPL+ and LGPL+
Group: Development/C++
URL: http://libbt.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/libbt/libbt-%{version}.tar.gz
Patch: libbt-1.06-header.patch
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
%patch -p1

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


