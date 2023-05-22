#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksnakeduel
Version  : 23.04.1
Release  : 53
URL      : https://download.kde.org/stable/release-service/23.04.1/src/ksnakeduel-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/ksnakeduel-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/ksnakeduel-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: ksnakeduel-bin = %{version}-%{release}
Requires: ksnakeduel-data = %{version}-%{release}
Requires: ksnakeduel-license = %{version}-%{release}
Requires: ksnakeduel-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the ksnakeduel package.
Group: Binaries
Requires: ksnakeduel-data = %{version}-%{release}
Requires: ksnakeduel-license = %{version}-%{release}

%description bin
bin components for the ksnakeduel package.


%package data
Summary: data components for the ksnakeduel package.
Group: Data

%description data
data components for the ksnakeduel package.


%package doc
Summary: doc components for the ksnakeduel package.
Group: Documentation

%description doc
doc components for the ksnakeduel package.


%package license
Summary: license components for the ksnakeduel package.
Group: Default

%description license
license components for the ksnakeduel package.


%package locales
Summary: locales components for the ksnakeduel package.
Group: Default

%description locales
locales components for the ksnakeduel package.


%prep
%setup -q -n ksnakeduel-23.04.1
cd %{_builddir}/ksnakeduel-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684781047
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684781047
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksnakeduel
cp %{_builddir}/ksnakeduel-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ksnakeduel/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/ksnakeduel-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksnakeduel/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ksnakeduel-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksnakeduel/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/ksnakeduel-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/ksnakeduel/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/ksnakeduel-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksnakeduel/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang ksnakeduel
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ksnakeduel
/usr/bin/ksnakeduel

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksnakeduel.desktop
/usr/share/config.kcfg/ksnakeduel.kcfg
/usr/share/icons/hicolor/128x128/apps/ksnakeduel.png
/usr/share/icons/hicolor/16x16/apps/ksnakeduel.png
/usr/share/icons/hicolor/22x22/apps/ksnakeduel.png
/usr/share/icons/hicolor/256x256/apps/ksnakeduel.png
/usr/share/icons/hicolor/32x32/apps/ksnakeduel.png
/usr/share/icons/hicolor/48x48/apps/ksnakeduel.png
/usr/share/icons/hicolor/64x64/apps/ksnakeduel.png
/usr/share/knsrcfiles/ksnakeduel.knsrc
/usr/share/ksnakeduel/themes/default.desktop
/usr/share/ksnakeduel/themes/default.png
/usr/share/ksnakeduel/themes/default.svgz
/usr/share/ksnakeduel/themes/neon.desktop
/usr/share/ksnakeduel/themes/neon.png
/usr/share/ksnakeduel/themes/neon.svgz
/usr/share/metainfo/org.kde.ksnakeduel.appdata.xml
/usr/share/qlogging-categories5/ksnakeduel.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/ca/ksnakeduel/index.docbook
/usr/share/doc/HTML/ca/ksnakeduel/settings-general.png
/usr/share/doc/HTML/ca/ksnakeduel/settings-theme.png
/usr/share/doc/HTML/en/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/en/ksnakeduel/index.docbook
/usr/share/doc/HTML/en/ksnakeduel/settings-general.png
/usr/share/doc/HTML/en/ksnakeduel/settings-theme.png
/usr/share/doc/HTML/es/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/es/ksnakeduel/index.docbook
/usr/share/doc/HTML/it/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/it/ksnakeduel/index.docbook
/usr/share/doc/HTML/nl/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/nl/ksnakeduel/index.docbook
/usr/share/doc/HTML/pt_BR/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksnakeduel/index.docbook
/usr/share/doc/HTML/sv/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/sv/ksnakeduel/index.docbook
/usr/share/doc/HTML/uk/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/uk/ksnakeduel/index.docbook
/usr/share/doc/HTML/uk/ksnakeduel/settings-general.png
/usr/share/doc/HTML/uk/ksnakeduel/settings-theme.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksnakeduel/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ksnakeduel/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/ksnakeduel/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/ksnakeduel/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/ksnakeduel/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f ksnakeduel.lang
%defattr(-,root,root,-)

