Summary:	A template based math C++ library for symbolic and numeric calculus applications
Summary(pl):	Matematyczna biblioteka szablon�w w C++ dla aplikacji symbolicznych i numerycznych
Name:		libmath++
Version:	0.0.3
Release:	1
License:	LGPL/GPL
Group:		Libraries
Source0:	http://www.surakware.net/pub/unstable/releases/libmath++/%{name}-%{version}.tar.gz
# Source0-md5:	f7d1bd1059b9620e5e9c8e2204430d3c
URL:		http://www.surakware.net/projects/libmath++/index.xml
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmath++ is a template based math library, written in C++, for
symbolic and numeric calculus applications.

%description -l pl
Libmath++ to matematyczna biblioteka szablon�w napisana w C++ dla
aplikacji symbolicznych i numerycznych.

%package devel
Summary:	libmath++ header files
Summary(pl):	Pliki nag��wkowe libmath++
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libmath++ header files.

%description devel -l pl
Pliki nag��wkowe libmath++.

%package static
Summary:	libmath++ static library
Summary(pl):	Statyczna biblioteka libmath++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libmath++ static library.

%description static -l pl
Statyczna biblioteka libmath++.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/math++

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
