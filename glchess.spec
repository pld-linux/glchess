Summary:	glChess - A 3D chess interface
Summary(pl):	glChess - Interfejs 3D do szachów
Name:		glchess
Version:	0.3.5
Release:	1
License:	GPL
Vendor:		Giuseppe Borzi' <gborzi@ieee.org>
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sf.net/glchess/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-xpm.tar.bz2
Patch0:		%{name}-patch2.patch
Patch1:		%{name}rc.patch
Patch2:		%{name}-dont_clear.patch
URL:		http://glchess.sf.net/
BuildRequires:	gtk+-devel
BuildRequires:	gtkglarea-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess
Engine Communication Protocol (CECP) by Tim Mann. This means it can
currently use Crafty and GNU Chess as AIs. You can also play Human vs.
Human, but so far not over a netwerk (see TODO).

%description -l pl
glChess to Trójwymiarowe (3D) szachy w technologii OpenGL. Program
u¿ywa Chess Engine Communication Protocol (CECP) autorstwa Tima Manna.
Oznacza to Crafty b±d¼ GNU Chess jako AI. Mo¿na tak¿e graæ cz³owiek
przeciw cz³owiekowi, lecz jeszcze nie przez sieæ (zobacz TODO).

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir}/glchess/textures} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_applnkdir}/Games,%{_pixmapsdir}}

install glchess $RPM_BUILD_ROOT%{_bindir}
install man/glchess.6 $RPM_BUILD_ROOT/%{_mandir}/man6
cp -rf textures $RPM_BUILD_ROOT%{_datadir}/glchess
install glchessrc $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

bzip2 -dc %{SOURCE2} | tar xvf -
install glchess-{16,32,48}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz AUTHORS.gz NEWS.gz TODO.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/glchess
%{_pixmapsdir}/*
%{_sysconfdir}/glchessrc
%{_applnkdir}/Games/glchess.desktop
