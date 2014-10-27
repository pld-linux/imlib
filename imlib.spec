Summary:	Image loading and rendering library for X11R6
Summary(es.UTF-8):	Biblioteca de carga y render 3D para X11R6
Summary(fr.UTF-8):	Librairie de chargement et interprétation d'images pour X11R6
Summary(ko.UTF-8):	X11R6를 위한 그림 읽기/화면에 그려주기 라이브러리
Summary(pl.UTF-8):	Biblioteki do renderowania i ładowania grafiki pod X11R6
Summary(pt_BR.UTF-8):	Biblioteca de carga e renderização para X11R6
Name:		imlib
Version:	1.9.15
Release:	24
Epoch:		1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/imlib/1.9/%{name}-%{version}.tar.bz2
# Source0-md5:	7db987e6c52e4daf70d7d0f471238eae
Source1:	%{name}-config.desktop
Patch0:		%{name}-m4_fix.patch
Patch1:		%{name}-full_i18n.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-am18.patch
Patch4:		%{name}-intl.patch
Patch5:		%{name}-CAN-2004-1026.patch
Patch6:		%{name}-link.patch
Patch7:		%{name}-16bit_depth_fix.patch
Patch8:		%{name}-exa_fix.patch
Patch9:		%{name}-ac.patch
Patch10:	%{name}-libpng.patch
Patch11:	%{name}-libpng15.patch
Patch12:	%{name}-giflib.patch
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel >= 5
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	libjpeg-devel >= 6b-18
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Obsoletes:	libimlib1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
Imlib is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexability and
speed.

%description -l es.UTF-8
Imlib es una biblioteca avanzada que sustituye las bibliotecas libXpm
que ofrece mucho más opciones/características con una flexibilidad y
velocidad mucho mayores.

%description -l fr.UTF-8
Imlib est une librairie de remplacement avancée pour les librairies
comme libXpm qui fourni plus d'atouts et beaucoup plus de flexibilité
et de vitesse.

%description -l pl.UTF-8
Imlib jest zaawansowanym zamiennikiem bibliotek typu libXpm, ze
zwiększoną elastycznością oraz prędkością.

%description -l pt_BR.UTF-8
A imlib é uma biblioteca avançada que substitui as bibliotecas libXpm
que fornece muito mais opções/características com uma flexibilidade e
velocidade muito maiores.

%package cfgeditor
Summary:	Imlib configuration editor
Summary(es.UTF-8):	Editor de configuración de imlib
Summary(ko.UTF-8):	Imlib라이브러리용 설정 편집기
Summary(pl.UTF-8):	Edytor konfiguracji do biblioteki imlib
Summary(pt_BR.UTF-8):	Editor da configuração da imlib
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description cfgeditor
The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%description cfgeditor -l es.UTF-8
El programa imlib_config te permite controlar como imlib usa los
colores y manipula la corrección gamma, etc.

%description cfgeditor -l pl.UTF-8
Program imlib_config umożliwia zmianę sposobu używania przez
bibliotekę imlib kolorów, korekcji gamma i innych.

%description cfgeditor -l pt_BR.UTF-8
O programa imlib_config lhe permite controlar como a imlib usa as
cores e trata correção gamma, etc.

%package devel
Summary:	Imlib header files and development documentation
Summary(es.UTF-8):	Archivos de inclusión, bibliotecas y documentación para Imlib
Summary(fr.UTF-8):	Fichiers entête pour Imlib
Summary(ko.UTF-8):	Imlib 응용프로그램들을 위한 개발 도구
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentacja do imlib
Summary(pt_BR.UTF-8):	Arquivos de inclusão, bibliotecas e documentação para a Imlib
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	giflib-devel >= 5
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	xorg-lib-libX11-devel
Requires:	zlib-devel
Obsoletes:	libimlib1-devel

%description devel
Header files and development documentation for Imlib.

%description devel -l es.UTF-8
Archivos de inclusión, bibliotecas estáticas y documentación para
imlib.

%description devel -l fr.UTF-8
Fichiers entête pour Imlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja do biblioteki Imlib.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão, bibliotecas estáticas e documentação para a
imlib.

%package static
Summary:	Imlib static libraries
Summary(pl.UTF-8):	Biblioteki statyczne imlib
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com imlib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Imlib static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne imlib.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com imlib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# temporary hack
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p0
%patch10 -p1
%patch11 -p0
%patch12 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# no static modules and *.la for modules - shut up check-files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libimlib-*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libImlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libImlib.so.1
%attr(755,root,root) %{_libdir}/libgdk_imlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk_imlib.so.1
%attr(755,root,root) %{_libdir}/libimlib-bmp.so
%attr(755,root,root) %{_libdir}/libimlib-gif.so
%attr(755,root,root) %{_libdir}/libimlib-jpeg.so
%attr(755,root,root) %{_libdir}/libimlib-png.so
%attr(755,root,root) %{_libdir}/libimlib-ppm.so
%attr(755,root,root) %{_libdir}/libimlib-ps.so
%attr(755,root,root) %{_libdir}/libimlib-tiff.so
%attr(755,root,root) %{_libdir}/libimlib-xpm.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/im_palette*.pal
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imrc

%files cfgeditor -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imlib_config
%{_mandir}/man1/imlib_config.1*
%{_desktopdir}/imlib-config.desktop

%files devel
%defattr(644,root,root,755)
%doc doc/{*.gif,*.html}
%attr(755,root,root) %{_bindir}/imlib-config
%attr(755,root,root) %{_libdir}/libImlib.so
%attr(755,root,root) %{_libdir}/libgdk_imlib.so
%{_libdir}/libImlib.la
%{_libdir}/libgdk_imlib.la
%{_includedir}/Imlib*.h
%{_includedir}/gdk_imlib*.h
%{_aclocaldir}/imlib.m4
%{_pkgconfigdir}/imlib.pc
%{_pkgconfigdir}/imlibgdk.pc
%{_mandir}/man1/imlib-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libImlib.a
%{_libdir}/libgdk_imlib.a
