Summary: 	glChess - A 3D chess interface
Summary(pl):	glChess - Interfejs 3D do szachów
Name: 		glchess
Version: 	0.3.5
Release: 	1
License: 	GPL
Group: 		Amusements/Games
Group(pl):	Aplikacje/Gry
Vendor:		Giuseppe Borzi' <gborzi@ieee.org>
URL: 		http://glchess.sf.net
Source: 	http://download.sf.net/glchess/%{name}-%{version}.tar.gz
Source1: 	glchess.menu
Patch0:		glchess-patch2.patch
Patch1: 	glchessrc.patch
BuildRequires:	gtk+-devel
BuildRequires:	gtkglarea-devel
BuildRoot: 	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently use
Crafty and GNU Chess as AIs. You can also play Human vs. Human, but so far
not over a netwerk (see TODO).

%description -l pl
glChess to Trójwymiarowe (3D) szachy w technologii OpenGL. Program u¿ywa 
Chess Engine Communication Protocol (CECP) autorstwa Tim'a Mann'a. Oznacza
to Crafty b±d¼ GNU Chess jako AI. Mo¿na tak¿e graæ cz³owiek przeciw cz³owiekowi,
lecz jeszcze nie przez sieæ (zobacz TODO).

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/games/glchess/textures
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/etc
cp glchess $RPM_BUILD_ROOT/%{_bindir}
cp man/glchess.6.gz $RPM_BUILD_ROOT/%{_mandir}/man6
cp -r textures $RPM_BUILD_ROOT/%{_datadir}/games/glchess/
cp glchessrc $RPM_BUILD_ROOT/etc
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS TODO
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/games/glchess/textures/*
/etc/glchessrc
%{_sysconfdir}/X11/wmconfig/*
