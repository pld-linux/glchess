Summary:	glChess - A 3D chess interface
Summary(pl):	glChess - Interfejs 3D do szachów
Name:		glchess
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/glchess/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}rc.patch
Patch1:		%{name}-CC_and_CFLAGS.patch
URL:		http://glchess.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreqdep   libGL.so.1 libGLU.so.1 libGLcore.so.1
%define         _noreqdep  	 libGL.so.1 libGLU.so.1 libGLcore.so.1
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
%patch1 -p1
find . -type d -name CVS -exec rm -rf {} \; ||:

%build
CFLAGS_FROM_RPM="%{rpmcflags}"
CC_FROM_RPM="%{__cc}"
export CFLAGS_FROM_RPM CC_FROM_RPM
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-lib-GL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir}/games/glchess/textures} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_applnkdir}/Games/Board,%{_pixmapsdir}}

install src/glchess	$RPM_BUILD_ROOT%{_bindir}
install man/glchess.6	$RPM_BUILD_ROOT%{_mandir}/man6
cp -rf textures		$RPM_BUILD_ROOT%{_datadir}/games/glchess
install glchessrc	$RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/Games/Board
install %{SOURCE2}	$RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/games/glchess
%{_pixmapsdir}/*
#Have to overwrite config since some options have been added.
%{_sysconfdir}/glchessrc
%{_applnkdir}/Games/Board/glchess.desktop
