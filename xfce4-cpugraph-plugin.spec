Summary:	Displays a graph from your latest system load
Summary(pl.UTF-8):	Wyświetlanie wykresu bieżącego obciążenia systemu
Name:		xfce4-cpugraph-plugin
Version:	0.4.0
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-cpugraph-plugin/%{name}-%{version}.tar.gz
# Source0-md5:	246697fc1e1ec5009aea34d4ef1dca95
Patch0:		%{name}-locale-names.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This systemload plugin offers multiple display modes (LED, gradient,
fire, etc.) to show the current CPU load of the system. The colors and
the size of the plugin are customizable.

%description -l pl.UTF-8
Ta wtyczka obciążenia systemu oferuje liczne tryby wyświetlania (ekran
ciekłokrystaliczny LED, gradient, ogień, itp.) aktualnego obciążenia
procesora. Kolory i rozmiar wtyczki są modyfikowalne.

%prep
%setup -q
%patch0 -p1

mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-cpugraph-plugin
%{_datadir}/xfce4/panel-plugins/cpugraph.desktop
