Summary:	Displays a graph from your latest system load
Summary(pl.UTF-8):	Wyświetlanie wykresu bieżącego obciążenia systemu
Name:		xfce4-cpugraph-plugin
Version:	1.3.0
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-cpugraph-plugin/1.3/%{name}-%{version}.tar.xz
# Source0-md5:	08594597c251da43fae297b325626001
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16
BuildRequires:	libxfce4util-devel >= 4.17.2
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
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

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# for dependency generator
chmod 755 $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.so

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libcpugraph.so
%{_datadir}/xfce4/panel/plugins/cpugraph.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
