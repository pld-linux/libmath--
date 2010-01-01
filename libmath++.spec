Summary:	A template based math C++ library for symbolic and numeric calculus applications
Summary(pl.UTF-8):	Matematyczna biblioteka szablonów w C++ dla aplikacji symbolicznych i numerycznych
Name:		libmath++
Version:	0.0.4
Release:	1
License:	LGPL/GPL
Group:		Libraries
#Source0:	http://upstream.trapni-akane.org/libmath++/%{name}-%{version}.tar.gz
Source0:	http://ftp.debian.org/debian/pool/main/libm/libmath++/%{name}_%{version}.orig.tar.gz
# Source0-md5:	ef2933a45df4def2d0a37f560399c9ad
Patch0:		%{name}-opt.patch
URL:		http://upstream.trapni-akane.org/libmath++/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmath++ is a template based math library, written in C++, for
symbolic and numeric calculus applications.

%description -l pl.UTF-8
Libmath++ to matematyczna biblioteka szablonów napisana w C++ dla
aplikacji symbolicznych i numerycznych.

%package devel
Summary:	libmath++ header files
Summary(pl.UTF-8):	Pliki nagłówkowe libmath++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libmath++ header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libmath++.

%package static
Summary:	libmath++ static library
Summary(pl.UTF-8):	Statyczna biblioteka libmath++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libmath++ static library.

%description static -l pl.UTF-8
Statyczna biblioteka libmath++.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libmath++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmath++.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmath++.so
%{_libdir}/libmath++.la
%{_includedir}/math++
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libmath++.a
