Summary:	Image loading and rendering library for X11R6
Summary(fr):	Librairie de chargement et interpr�tation d'images pour X11R6
Summary(pl):	Biblioteki do renderowania i �adowania grafiki pod X11R6
Name:		imlib
Version:	1.9.8
Release:	4
License:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/imlib/%{name}-%{version}.tar.gz
Source1:	imlib-config.desktop
Patch:		imlib-gdk.patch
URL:		http://www.labs.redhat.com/imlib/
BuildRequires:	glib-devel 
BuildRequires:	gtk+-devel 
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_datadir	/usr/share
%define		_sysconfdir	/etc/X11

%description
Imlib is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexability and speed.

%description -l fr
Imlib est une librairie de remplacement avanc�e pour les librairies comme
libXpm qui fourni plus d'atouts et beaucoup plus de flexibilit� et de
vitesse.

%description -l pl
Imlib jest zaawansowanym zamiennikiem bibliotek typu libXpm.

%package cfgeditor
Summary:	Imlib configuration editor
Summary(pl):	Edytor konfiguracji do biblioteki imlib
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Requires:	%{name} = %{version}

%description cfgeditor
The imlib_config program allows you to control the way imlib uses color and
handles gamma correction/etc.

%description -l pl cfgeditor
Program imlib_config umo�liwia zmian� sposobu u�ywania przez bibliotek�
imlib kolor�w, korekcji gamma i innych.  The imlib_config program allows
you to control the way imlib uses color and handles gamma correction/etc.

%package devel
Summary:	Imlib header files and development documentation
Summary(fr):	Fichiers ent�te pour Imlib
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
# Every program using imlib should get a list of libraries to link with by
# executing `imlib-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with imlib.
Requires:	libjpeg-devel
Requires:	libtiff-devel
Requires:	libungif-devel
Requires:	libpng-devel
Requires:	zlib-devel
Requires	XFree86-devel

%description devel
Header files and development documentation for Imlib.

%description devel -l fr
Fichiers ent�te pour Imlib.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki Imlib.

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
%patch0 -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure

make
			    
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so{,.*.*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libImlib.so.*.*
%attr(755,root,root) %{_libdir}/libgdk_imlib.so.*.*
%attr(755,root,root) %{_libdir}/libimlib-*.so
%attr(755,root,root) %{_libdir}/libimlib-*.la
%config %{_sysconfdir}/*

%files cfgeditor
%defattr(644,root,root,755)
%{_applnkdir}/Settings/imlib-config.desktop
%attr(755,root,root) %{_bindir}/imlib_config

%files devel
%defattr(644,root,root,755)
%doc doc/{*gif,*.html}

%attr(755,root,root) %{_libdir}/libImlib.so
%attr(755,root,root) %{_libdir}/libgdk_imlib.so
%attr(755,root,root) %{_libdir}/libImlib.la
%attr(755,root,root) %{_libdir}/libgdk_imlib.la

%attr(755,root,root) %{_bindir}/imlib-config

%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%defattr(644,root,root,755)

%{_libdir}/lib*.a
