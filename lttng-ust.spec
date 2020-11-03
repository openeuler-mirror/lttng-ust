Name:           lttng-ust
Version:        2.10.1
Release:        9
Summary:        LTTng Userspace Tracer library
License:        LGPLv2 and GPLv2 and MIT
URL:            https://lttng.org

Source0:        https://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2
Patch0:         Fix-namespace-our-gettid-wrapper.patch
Patch1:         lttng-gen-tp-shebang.patch

BuildRequires:  libuuid-devel autoconf automake libtool
BuildRequires:  userspace-rcu-devel >= 0.8.0

%description
This library is used by user-space applications to generate trace-points using LTTng.

%package -n %{name}-devel
Summary:        LTTng Userspace Tracer library headers and development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       userspace-rcu-devel

%package_help

%description -n %{name}-devel
The devel for %{name}

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -vif

%configure --docdir=%{_docdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
make check

%files
%{_libdir}/*.so.*
%exclude %{_libdir}/*.la

%files -n %{name}-devel
%{_bindir}/lttng-gen-tp
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ust*.pc
%{_docdir}/%{name}/examples/*

%files help
%{_mandir}/man1/lttng-gen-tp.1.gz
%{_mandir}/man3/*.gz
%{_docdir}/%{name}/*

%changelog
* Mon Nov 02 2020 xinghe <xinghe1@huawei.com> - 2.10.1-9
- fix lttng-gen-tp command

* Fri Oct 30 2020 xinghe <xinghe1@huawei.com> - 2.10.1-8
- remove python2 dependency

* Thu Jul 30 2020 jinzhimin<jinzhimin2@huawei.com> - 2.10.1-7
- Add patch to build on glibc >= 2.30

* Fri Feb 14 2020 liuchao <liuchao173@huawei.com> - 2.10.1-6
- enable make check

* Thu Aug 15 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.10.1-5
- Package init

