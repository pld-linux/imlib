Summary:     Image loading and rendering library for X11R6
Summary(pl): Biblioteki do renderowania i ³adowania plików graficznych pod X'y
Name:        imlib 
Version:     1.8.1
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.labs.redhat.com/pub/imlib/TAR/%{name}-%{version}.tar.gz
Requires:    libpng, libtiff, libjpeg, zlib, libgr-progs, glib, gtk+, libungif
Requires:    libungif, ImageMagick
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
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--sysconfdir=/etc \
	--datadir=/usr/share
make
			    
%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	sysconfdir=$RPM_BUILD_ROOT/etc \
	datadir=$RPM_BUILD_ROOT/usr/share
strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*
strip $RPM_BUILD_ROOT/usr/X11R6/{bin/imlib_config,lib/lib*.so.*.*}
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
/usr/X11R6/lib/lib*.so
/usr/share/aclocal/*
%attr(755, root, root) /usr/X11R6/bin/imlib-config

%files static
%attr(644, root, root) /usr/X11R6/lib/*a

%changelog
* Sun Jan 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
