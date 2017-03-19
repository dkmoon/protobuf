%global commit0 %{COMMIT_ID}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           protobuf
Version:        3.1.0
Release:	%{shortcommit0}%{dist}
Summary:	Google Protobuf
Group:		Development/Libraries
License:	MIT
URL:      https://github.com/google/protobuf
Source0:	protobuf-%{COMMIT_ID}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}%{dist}-XXXXXX)
BuildRequires:	autoconf, automake, libtool, make, rpm-build
Requires:	boost-date-time, boost-random, boost-system, cmake, make, openssl-devel

%description
Protocol Buffers are a way of encoding structured data in an efficient
yet extensible format. Google uses Protocol Buffers for almost all of
its internal RPC protocols and file formats.

Protocol buffers are a flexible, efficient, automated mechanism for
serializing structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be structured once, then
you can use special generated source code to easily write and read
your structured data to and from a variety of data streams and using a
variety of languages. You can even update your data structure without
breaking deployed programs that are compiled against the "old" format.


#%define debug_package %{nil}


%prep
%setup -q -n protobuf


%build
./autogen.sh
mkdir rpm_build_result
pushd rpm_build_result
../configure --prefix=/usr
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd rpm_build_result
DESTDIR=%{buildroot} make install
popd


%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,root,0755)
/usr/lib/libprotobuf.so.12.0.0
/usr/lib/libprotobuf.so.12
/usr/lib/libprotobuf-lite.so.12.0.0
/usr/lib/libprotobuf-lite.so.12


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



%package devel
Summary:	Protocol Buffers C++ headers and libraries
Group:		Development/Libraries
Requires:       protobuf = %{version}-%{release}, protobuf-compiler = %{version}-%{release}


%description devel
This package contains Protocol Buffers compiler for all languages and
C++ headers and libraries


%files devel
%defattr(0644,root,root,0755)
/usr/include/google/protobuf/
/usr/lib/pkgconfig/protobuf-lite.pc
/usr/lib/pkgconfig/protobuf.pc
%defattr(0755,root,root,0755)
/usr/lib/libprotobuf.a
/usr/lib/libprotobuf.la
/usr/lib/libprotobuf.so
/usr/lib/libprotobuf-lite.a
/usr/lib/libprotobuf-lite.la
/usr/lib/libprotobuf-lite.so
/usr/lib/libprotoc.so


%post devel
/sbin/ldconfig


%postun devel
/sbin/ldconfig



%package compiler
Summary:	Protocol Buffers compiler
Group:		Development/Libraries
Requires:       protobuf = %{version}-%{release}


%description compiler
This package contains Protocol Buffers compiler for all programming
languages


%files compiler
%defattr(0755,root,root,0755)
/usr/bin/protoc
/usr/lib/libprotoc.so.12.0.0
/usr/lib/libprotoc.so.12
/usr/lib/libprotoc.la
/usr/lib/libprotoc.a


%post compiler
/sbin/ldconfig


%postun compiler
/sbin/ldconfig



#%changelog
