#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gupnp-av
Version  : 0.12.11
Release  : 10
URL      : https://download.gnome.org/sources/gupnp-av/0.12/gupnp-av-0.12.11.tar.xz
Source0  : https://download.gnome.org/sources/gupnp-av/0.12/gupnp-av-0.12.11.tar.xz
Summary  : Library to ease handling and implementation of UPnP A/V profiles
Group    : Development/Tools
License  : LGPL-2.0
Requires: gupnp-av-data = %{version}-%{release}
Requires: gupnp-av-lib = %{version}-%{release}
Requires: gupnp-av-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : vala

%description
GUPnP A/V
=========
GUPnP is an object-oriented open source framework for creating UPnP devices and
control points, written in C using GObject and libsoup. The GUPnP API is
intended to be easy to use, efficient and flexible.

%package data
Summary: data components for the gupnp-av package.
Group: Data

%description data
data components for the gupnp-av package.


%package dev
Summary: dev components for the gupnp-av package.
Group: Development
Requires: gupnp-av-lib = %{version}-%{release}
Requires: gupnp-av-data = %{version}-%{release}
Provides: gupnp-av-devel = %{version}-%{release}
Requires: gupnp-av = %{version}-%{release}

%description dev
dev components for the gupnp-av package.


%package doc
Summary: doc components for the gupnp-av package.
Group: Documentation

%description doc
doc components for the gupnp-av package.


%package lib
Summary: lib components for the gupnp-av package.
Group: Libraries
Requires: gupnp-av-data = %{version}-%{release}
Requires: gupnp-av-license = %{version}-%{release}

%description lib
lib components for the gupnp-av package.


%package license
Summary: license components for the gupnp-av package.
Group: Default

%description license
license components for the gupnp-av package.


%prep
%setup -q -n gupnp-av-0.12.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557013679
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557013679
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gupnp-av
cp COPYING %{buildroot}/usr/share/package-licenses/gupnp-av/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gupnp-av/av.xsd
/usr/share/gupnp-av/didl-lite-v2.xsd
/usr/share/gupnp-av/simpledc20021212.xsd
/usr/share/gupnp-av/upnp.xsd
/usr/share/gupnp-av/xml.xsd
/usr/share/vala/vapi/gupnp-av-1.0.deps
/usr/share/vala/vapi/gupnp-av-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-av-enums.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-av-error.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-av.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-cds-last-change-parser.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-container.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-contributor.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-createclass.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-descriptor.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-item.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-object.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-parser.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-resource.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-didl-lite-writer.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-dlna.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-feature-list-parser.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-feature.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-last-change-parser.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-media-collection.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-protocol-info.h
/usr/include/gupnp-av-1.0/libgupnp-av/gupnp-search-criteria-parser.h
/usr/lib64/libgupnp-av-1.0.so
/usr/lib64/pkgconfig/gupnp-av-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gupnp-av/GUPnPCDSLastChangeParser.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteContainer.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteContributor.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteDescriptor.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteItem.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteObject.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteParser.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteResource.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPDIDLLiteWriter.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPFeature.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPFeatureListParser.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPLastChangeParser.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPMediaCollection.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPProtocolInfo.html
/usr/share/gtk-doc/html/gupnp-av/GUPnPSearchCriteriaParser.html
/usr/share/gtk-doc/html/gupnp-av/annotation-glossary.html
/usr/share/gtk-doc/html/gupnp-av/ch01.html
/usr/share/gtk-doc/html/gupnp-av/ch02.html
/usr/share/gtk-doc/html/gupnp-av/gupnp-av-Error-codes.html
/usr/share/gtk-doc/html/gupnp-av/gupnp-av-GUPnPDIDLLiteCreateClass.html
/usr/share/gtk-doc/html/gupnp-av/gupnp-av.devhelp2
/usr/share/gtk-doc/html/gupnp-av/home.png
/usr/share/gtk-doc/html/gupnp-av/index.html
/usr/share/gtk-doc/html/gupnp-av/left-insensitive.png
/usr/share/gtk-doc/html/gupnp-av/left.png
/usr/share/gtk-doc/html/gupnp-av/right-insensitive.png
/usr/share/gtk-doc/html/gupnp-av/right.png
/usr/share/gtk-doc/html/gupnp-av/style.css
/usr/share/gtk-doc/html/gupnp-av/up-insensitive.png
/usr/share/gtk-doc/html/gupnp-av/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgupnp-av-1.0.so.2
/usr/lib64/libgupnp-av-1.0.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gupnp-av/COPYING
