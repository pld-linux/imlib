Summary:	Image loading and rendering library for X11R6
Summary(pl):	Biblioteki do renderowania i ³adowania grafiki pod X11R6
Name:		imlib 
Version:	1.9.5
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/source/imlib/%{name}/%{name}-%{version}.tar.gz
Patch:		imlib-16bppgrabfix.patch
URL:		http://www.labs.redhat.com/imlib/
BuildPrereq:	glib-devel 
BuildPrereq:	gtk+-devel 
BuildPrereq:	XFree86-devel
BuildPrereq:	libjpeg-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libpng-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_datadir	/usr/share
%define		_sysconfdir	/etc/X11

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
Group(pl):	X11/Narzêdzia
Requires:	%{name} = %{version}

%description cfgeditor
The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%description -l pl cfgeditor
Program imlib_config umo¿liwia zmianê sposobu u¿ywania przez bibliotekê
imlib kolorów, korekcji gamma i innych.

The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%package devel
Summary:	Imlib header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for Imlib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki Imlib.

%package static
Summary:	Imlib static libraries
Summary(pl):	Biblioteki statyczne imlib
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Imlib static libraries.

%description devel -l pl
Biblioteki statyczne imlib.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make
			    
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*
%config /etc/X11/*

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
* Mon May 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.4-3]
- spec based on RH version,
- rewrirted by Piotr Czerwiñski <pius@pld.org.pl> and me,
- pl translation Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
