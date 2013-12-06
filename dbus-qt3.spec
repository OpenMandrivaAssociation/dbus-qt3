%define dbus_version		0.90
%define qt_version              3.1.0
%define qt_dir			%{_prefix}/lib/qt3

%define lib_api 1
%define lib_qt_major 1
%define lib_qt %mklibname dbus-qt- %{lib_api} %{lib_qt_major}
%define devel_qt %mklibname dbus-qt -d

Summary: D-BUS message bus
Name: dbus-qt3
Version: 0.70
Release: 12
URL: http://www.freedesktop.org/Software/dbus
Source0: %{name}-%{version}.tar.bz2
Patch0:	dbus-qt3-underlinking.patch
Patch1:	dbus-qt3-automake-1.13.patch

License: AFL/GPL
Group: System/Servers
BuildRequires: qt3-devel    >= %{qt_version}
BuildRequires: dbus-devel >= %{dbus_version}

%package -n %{lib_qt}
Summary: Qt-based library for using D-BUS
Group: System/Libraries
Obsoletes: %{_lib}dbus-qt-1_0 < 0.62-2mdv2007.0

%description -n %{lib_qt}
D-BUS add-on library to integrate the standard D-BUS library with
the Qt thread abstraction and main loop.

%package -n %{devel_qt}
Summary: Qt-based library for using D-BUS
Group: Development/C++
Requires: %{lib_qt} = %{version}-%{release}
Provides: libdbus-qt-1-devel = %{version}-%{release}
Obsoletes: %mklibname dbus-qt- %{lib_api} %{lib_qt_major} -d
Provides: %mklibname dbus-qt- %{lib_api} %{lib_qt_major} -d

%description -n %{devel_qt}
D-BUS add-on library to integrate the standard D-BUS library with the
Qt thread abstraction and main loop. This contains the Qt specific
headers and libraries.

%description
D-BUS add-on library to integrate the standard D-BUS library with
the Qt thread abstraction and main loop.

%prep
%setup -q 
%apply_patches

%build
autoreconf -fi

#gw so we can find moc
export PATH=%qt_dir/bin:$PATH
export QTDIR=%qt_dir

%configure2_5x --enable-qt3
%make

%install
rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged file
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_qt} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_qt} -p /sbin/ldconfig
%endif

%files -n %{lib_qt}
%defattr(-,root,root)
%{_libdir}/*qt*.so.%{lib_qt_major}*

%files -n %{devel_qt}
%defattr(-,root,root)
%{_libdir}/*qt*.so
%{_libdir}/*qt*.a
%{_includedir}/dbus-1.0/dbus/dbus-qt.h
%{_includedir}/dbus-1.0/dbus/connection.h
%{_includedir}/dbus-1.0/dbus/message.h
%{_includedir}/dbus-1.0/dbus/server.h


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.70-8mdv2011.0
+ Revision: 663759
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.70-7mdv2011.0
+ Revision: 604781
- rebuild

* Sun Mar 15 2009 Anssi Hannula <anssi@mandriva.org> 0.70-6mdv2010.1
+ Revision: 355363
- fix underlinking (underlinking.patch)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.70-4mdv2008.1
+ Revision: 154677
- Bump release for rebuild.

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.70-3mdv2008.1
+ Revision: 149166
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.70-2mdv2008.0
+ Revision: 60163
- rebuild
- new devel library policy


* Mon Mar 12 2007 Frederic Crozat <fcrozat@mandriva.com> 0.70-1mdv2007.1
+ Revision: 141612
- Add Obsoletes to ease upgrade from 2006.0
- Import dbus-qt3

* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.70-1mdv2007.0
- Initial package (splitted from dbus 0.62)

