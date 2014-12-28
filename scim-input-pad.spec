Summary:	SCIM Input Pad
Summary(pl.UTF-8):	SCIM Input Pad - panel do wprowadzania znaków dla SCIM
Name:		scim-input-pad
Version:	0.1.3.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	7ab0a700f5f4bd66f8f8138070d2abd4
Patch0:		%{name}-data.patch
URL:		http://www.scim-im.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	scim-devel >= 1.2.0
Requires:	gtk+2 >= 2:2.4.0
Requires:	scim >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM Input Pad is an onscreen input pad used to input some symbols
very easily.

%description -l pl.UTF-8
SCIM Input Pad to wyświetlany na ekranie panel służący do łatwego
wprowadzania różnych symboli.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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

# dlopened module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la
# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libscim-input-pad.{so,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/scim-input-pad
%attr(755,root,root) %{_libdir}/libscim-input-pad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libscim-input-pad.so.0
%attr(755,root,root) %{_libdir}/scim-1.0/*/Helper/input-pad.so
%{_datadir}/scim/icons/input-pad.png
%{_datadir}/scim/input-pad
