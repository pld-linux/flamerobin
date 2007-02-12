Summary:	Database administration tool for Firebird DBMS
Summary(pl.UTF-8):	Narzędzie do administrowania bazy danych dla Firebirda
Name:		flamerobin
Version:	0.7.6
Release:	1
License:	BSD-like
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/flamerobin/%{name}-%{version}-src.tar.gz
# Source0-md5:	8ef6c222b162a0e2b24ee8b54380491c
URL:		http://flamerobin.sourceforge.net/
BuildRequires:	Firebird-devel
BuildRequires:	autoconf
BuildRequires:	bakefile
BuildRequires:	ibpp-devel
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlameRobin is a database administration tool for Firebird DBMS. It was
designed as a tool that is:
- lightweight (small footprint, fast execution),
- cross-platform (Linux, Windows, MacOS X, FreeBSD, Solaris),
- dependent only on other Open Source software.

%description -l pl.UTF-8
FlameRobin to narzędzie do administrowania bazami danych dla systemu
baz danych (DBMS) Firebird. Zostało zaprojektowane jako narzędzie:
- lekkie (mały narzut, szybkie wykonywanie)
- wieloplatformowe (Linux, Windows, MacOS X, FireBSD, Solaris)
- zależne tylko od innego oprogramowania Open Source

%prep
%setup -q -n %{name}-%{version}-src

%build
bakefile_gen
%{__aclocal}
%{__autoconf}
%configure \
	WX_CONFIG_NAME=/usr/bin/wx-gtk2-ansi-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/flamerobin
%{_mandir}/man?/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
