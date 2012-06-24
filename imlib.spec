Summary:	Image loading and rendering library for X11R6
Summary(pl):	Biblioteki do renderowania i �adowania plik�w graficznych pod X'y
Name:		imlib 
Version:	1.9.4
Release:	3
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/source/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.labs.redhat.com/imlib/
BuildPrereq:	glib-devel >= 1.1.9
BuildPrereq:	gtk+-devel >= 1.1.9
BuildPrereq:	XFree86-devel
BuildPrereq:	libjpeg-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libpng-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	Imlib

%define _prefix  /usr/X11R6
%define _datadir /usr/share

%description
Imlib is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexability and
speed.

%description -l pl
Imlib jest zaawansowanym zamiennikiem bibliotek typu libXpm.

%package cfgeditor
Summary:	Imlib configuration editor
Summary(pl):	Edytor konfiguracji do biblioteki imlib
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Requires:	%{name} = %{version}

%description cfgeditor
The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%description -l pl cfgeditor
Program imlib_config umo�liwia zmian� sposobu u�ywania przez bibliotek�
imlib kolor�w, korekcji gamma i innych.

The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%package devel
Summary:	Imlib header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	Imlib

%description devel
Header files and development documentation for Imlib.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki Imlib.

%package static
Summary:	Imlib static libraries
Summary(pl):	Biblioteki statyczne imlib
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	Imlib

%description static
Imlib static libraries.

%description devel -l pl
Biblioteki statyczne imlib.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=/etc/X11/GNOME \
	--datadir=%{_datadir}
make
			    
%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(644,root,root) %config /etc/X11/GNOME/*

%files cfgeditor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imlib_config

%files devel
%defattr(644,root,root,755)
%doc doc/{*gif,*.html}
%attr(755,root,root) %{_libdir}/lib*.so

%attr(755,root,root) %{_bindir}/imlib-config

%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Mon May 24 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.4-3]
- spec based on RH version,
- rewrirted by Piotr Czerwi�ski <pius@pld.org.pl> and me,
- pl translation Wojtek �lusarczyk <wojtek@shadow.eu.org>.
