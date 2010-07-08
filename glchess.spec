Summary:	glChess - A 3D chess interface
Summary(pl.UTF-8):	glChess - Interfejs 3D do szachów
Name:		glchess
Version:	1.0.6
Release:	4
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/glchess/%{name}-%{version}.tar.gz
# Source0-md5:	b0125b7b824f2e4012badd0c465444dd
URL:		http://live.gnome.org/glChess
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires(post,preun):	GConf2
Requires:	python-gnome-gconf
Suggests:	python-PyOpenGL
Suggests:	python-pygtkglext >= 1.1.0-2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
Conflicts:	gnome-games-glchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_noreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess
Engine Communication Protocol (CECP) by Tim Mann. This means it can
currently use Crafty and GNU Chess as AIs. You can also play Human vs.
Human, but so far not over a netwerk (see TODO).

%description -l pl.UTF-8
glChess to Trójwymiarowe (3D) szachy w technologii OpenGL. Program
używa Chess Engine Communication Protocol (CECP) autorstwa Tima Manna.
Oznacza to Crafty bądź GNU Chess jako AI. Można także grać człowiek
przeciw człowiekowi, lecz jeszcze nie przez sieć (zobacz TODO).

%prep
%setup -q
find . -type d -name CVS -exec rm -rf {} \; ||:

sed -i -e s#sr\@Latn#sr\@latin# Makefile
mv po/sr\@{Latn,latin}.po

%build
%{__make}

%{__sed} -i -e 's#/usr/bin/python2.4#/usr/bin/python#' glchess

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{py_sitescriptdir}} \
	$RPM_BUILD_ROOT{%{_datadir}/games/%{name}/{gui,textures},%{_sysconfdir}/gconf/schemas}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install glchess	$RPM_BUILD_ROOT%{_bindir}
cp -rf lib/%{name} $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}
install glade/*.glade		$RPM_BUILD_ROOT%{_datadir}/games/%{name}/gui/
install data/ai.xml		$RPM_BUILD_ROOT%{_datadir}/games/%{name}
install data/textures/*		$RPM_BUILD_ROOT%{_datadir}/games/%{name}/textures/
install data/glchess.desktop	$RPM_BUILD_ROOT%{_desktopdir}
install data/glchess.svg	$RPM_BUILD_ROOT%{_pixmapsdir}
install data/glchess.schemas	$RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install glchess.schemas

%preun
%gconf_schema_uninstall glchess.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS ChangeLog README TODO tests
%{_sysconfdir}/gconf/schemas/glchess.schemas
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%dir %{py_sitescriptdir}/%{name}/chess
%{py_sitescriptdir}/%{name}/chess/*.py[co]
%dir %{py_sitescriptdir}/%{name}/chess/fics
%{py_sitescriptdir}/%{name}/chess/fics/*.py[co]
%dir %{py_sitescriptdir}/%{name}/ggz
%{py_sitescriptdir}/%{name}/ggz/*.py[co]
%dir %{py_sitescriptdir}/%{name}/gtkui
%{py_sitescriptdir}/%{name}/gtkui/*.py[co]
%dir %{py_sitescriptdir}/%{name}/scene
%{py_sitescriptdir}/%{name}/scene/*.py[co]
%dir %{py_sitescriptdir}/%{name}/scene/cairo
%{py_sitescriptdir}/%{name}/scene/cairo/*.py[co]
%dir %{py_sitescriptdir}/%{name}/scene/opengl
%{py_sitescriptdir}/%{name}/scene/opengl/*.py[co]
%dir %{py_sitescriptdir}/%{name}/ui
%{py_sitescriptdir}/%{name}/ui/*.py[co]
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*.xml
%dir %{_datadir}/games/%{name}/gui
%{_datadir}/games/%{name}/gui/*.glade
%dir %{_datadir}/games/%{name}/textures
%{_datadir}/games/%{name}/textures/*.png
%{_pixmapsdir}/*
%{_desktopdir}/glchess.desktop
