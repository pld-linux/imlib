Summary:     Image loading and rendering library for X11R6
Summary(pl): Biblioteki do renderowania i ³adowania plików graficznych pod X'y
Name:        imlib 
Version:     1.9.0
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Group(pl):   X11/Biblioteki
Source:      ftp://ftp.gnome.org/pub/GNOME/source/%{name}/%{name}-%{version}.tar.gz
Requires:    libpng, libtiff, libjpeg, zlib, libgr-progs, glib, gtk+, libungif
Requires:    gtk+ = 1.1.13, glib = 1.1.13, libungif, ImageMagick
URL:         http://www.labs.redhat.com/imlib/
Obsoletes:   Imlib
BuildRoot:   /tmp/%{name}-%{version}-root
%description
Imlib is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexability and
speed.

%description -l pl
Imlib jest zaawansowanym zamiennikiem bibliotek typu libXpm.

%package devel
Summary:	Imlib header files and development documentation
Summary:     Imlib header files and development documentation
Summary(pl): Pliki nag³ówkowe oraz dokumentacja do imlib
Group:       X11/Libraries
Group(pl):   X11/Biblioteki
Requires:    %{name} = %{version}
Obsoletes:   Imlib
%description devel
Header files and development documentation for Imlib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki Imlib.

%package static
Summary:	Imlib static libraries
Summary:     Imlib static libraries
Summary(pl): Biblioteki statyczne imlib
Group:       X11/Libraries
Group(pl):   X11/Biblioteki
Requires:    %{name}-devel = %{version}
Obsoletes:   Imlib
%description static
Imlib static libraries.

%description devel -l pl
Biblioteki statyczne imlib.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc \
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
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
%attr(644, root, root) %config /etc/*
%attr(755, root, root) /usr/X11R6/bin/imlib_config

%files devel
%defattr(644, root, root, 755)
%doc README doc
%attr(755, root, root) /usr/X11R6/lib/lib*.so
%attr(755, root, root) /usr/X11R6/bin/imlib-config
/usr/X11R6/include/*
/usr/share/aclocal/*

%files static
%attr(644, root, root) /usr/X11R6/lib/*a

%changelog
* Sun Jan 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
