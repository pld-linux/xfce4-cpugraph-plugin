# $Revision $, $Date $
Summary:	Displays a graph from your latest system load
Summary(pl):	Wy¶wietla wykres bie¿±cego obci±¿enia systemu
Name:		xfce4-cpugraph-plugin
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	bde4c578ef469aade3f6b58a9bde8ec6
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This systemload plugin offers multiple display modes (LED,
gradient, fire, etc.) to show the current CPU load of the
system. The colors and the size of the plugin are customizable.

%description -l pl
Ta wtyczka obci±¿enia systemu oferuje liczne tryby wy¶wietlania
(ekran ciek³okrystaliczny LED, gradient, ogieñ, itp.) aktualnego
obci±¿enia procesora. Kolory i rozmiar wtyczki s± modyfikowalne.

%prep
%setup -q -n %{name}

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
