Summary:	Image loading and rendering library for X11R6
Summary(fr):	Librairie de chargement et interprétation d'images pour X11R6
Summary(pl):	Biblioteki do renderowania i ³adowania grafiki pod X11R6
Name:		imlib
Version:	1.9.14
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/imlib/%{name}-%{version}.tar.bz2
Source1:	%{name}-config.desktop
Patch0:		%{name}-m4_fix.patch
Patch1:		%{name}-full_i18n.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-ac25x.patch
URL:		http://www.labs.redhat.com/imlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel >= 6b-18
BuildRequires:	libtiff-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	gdk-pixbuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
Imlib is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexability and
speed.

%description -l fr
Imlib est une librairie de remplacement avancée pour les librairies
comme libXpm qui fourni plus d'atouts et beaucoup plus de flexibilité
et de vitesse.

%description -l pl
Imlib jest zaawansowanym zamiennikiem bibliotek typu libXpm, ze
zwiêkszon± elastyczno¶ci± oraz prêdko¶ci±.

%package cfgeditor
Summary:	Imlib configuration editor
Summary(pl):	Edytor konfiguracji do biblioteki imlib
Group:		X11/Applications
Requires:	%{name} = %{version}

%description cfgeditor
The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%description cfgeditor -l pl
Program imlib_config umo¿liwia zmianê sposobu u¿ywania przez
bibliotekê imlib kolorów, korekcji gamma i innych.

%package devel
Summary:	Imlib header files and development documentation
Summary(fr):	Fichiers entête pour Imlib
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do imlib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
# Every program using imlib should get a list of libraries to link with by
# executing `imlib-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with imlib.
Requires:	libjpeg-devel
Requires:	libtiff-devel
Requires:	libungif-devel
Requires:	libpng-devel
Requires:	zlib-devel
Requires:	XFree86-devel

%description devel
Header files and development documentation for Imlib.

%description devel -l fr
Fichiers entête pour Imlib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki Imlib.

%package static
Summary:	Imlib static libraries
Summary(pl):	Biblioteki statyczne imlib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Imlib static libraries.

%description static -l pl
Biblioteki statyczne imlib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

%build
rm -rf missing
gettextize --copy --force
aclocal
autoconf
automake -a -c -f
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libImlib.so.*.*
%attr(755,root,root) %{_libdir}/libgdk_imlib.so.*.*
%attr(755,root,root) %{_libdir}/libimlib-*.so
%config %{_sysconfdir}/*

%files cfgeditor -f %{name}.lang
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
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
