Summary:	Image loading and rendering library for X11R6
Summary(pl):	Biblioteki do renderowania i ³adowania plików graficznych pod X'y
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
Obsoletes:	Imlib

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
Obsoletes:	Imlib

%description static
Imlib static libraries.

%description devel -l pl
Biblioteki statyczne imlib.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--datadir=/usr/share
make
			    
%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*
%attr(644,root,root) %config /etc/X11/GNOME/*

%files cfgeditor
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/imlib_config

%files devel
%defattr(644,root,root,755)
%doc doc/{*gif,*.html}
%attr(755,root,root) /usr/X11R6/lib/lib*.so

%attr(755,root,root) /usr/X11R6/bin/imlib-config

/usr/X11R6/include/*
/usr/share/aclocal/*

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%changelog
* Thu Apr 22 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.9.4-3]
- removed "Conflicts: glibc <= 2.0.7" (not neccessary now),
- removed old %requires_pkg_ver macros,
- added "BuildPrereq: XFree86-devel",
- minor changes,
- recompiles on rpm 3.

* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.4-2]
- updated Requires to glib = 1.2.1, gtk = 1.2.1.

* Sun Mar 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.4-1]
- removed Requires without versions which now are generated automatically.

* Wed Feb 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.3-1]
- updated Requires to glib = 1.2.0, gtk = 1.2.0,
- added "Conflicts: glibc <= 2.0.7" for preven installing with proper
  version glibc,
- added cfgeditor subpackage,
- updated Requires for gtk+/glib,
- changed sysconfdir to /etc/X11/GNOME.

* Sun Jan 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.2-1d]
- changed Group in devel and static subpackages,
- updated "Requires: gtk+ = 1.1.14, glib = 1.1.14".

* Tue Jan 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.0-1]
- added Group(pl),
- added "Requires: gtk+ = 1.1.13, glib = 1.1.13",
- changes in %install (use DESTDIR).

* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.8.1-1]
- added missing /usr/share/aclocal/* files to devel,
- files from /usr/etc moved to /etc and marked as %config,
- changed prefix to /usr/X11R6.

* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added full %attr description in %files,
- added stripping shared libraries and binarires,
- fixed passing $RPM_OPT_FLAGS,
- /usr/bin/imlib-config moved to devel,
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>).

* Fri Apr 3 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed typo

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Added -k, Obsoletes
- Integrate into CVS source tree
