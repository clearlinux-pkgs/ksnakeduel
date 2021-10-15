#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksnakeduel
Version  : 21.08.2
Release  : 32
URL      : https://download.kde.org/stable/release-service/21.08.2/src/ksnakeduel-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/ksnakeduel-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/ksnakeduel-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: ksnakeduel-bin = %{version}-%{release}
Requires: ksnakeduel-data = %{version}-%{release}
Requires: ksnakeduel-license = %{version}-%{release}
Requires: ksnakeduel-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n ksnakeduel-21.08.2
cd %{_builddir}/ksnakeduel-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634339225
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634339225
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksnakeduel
cp %{_builddir}/ksnakeduel-21.08.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/ksnakeduel/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/ksnakeduel-21.08.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksnakeduel/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang ksnakeduel

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/ksnakeduel/themes/neon.svg
/usr/share/metainfo/org.kde.ksnakeduel.appdata.xml
/usr/share/qlogging-categories5/ksnakeduel.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/de/ksnakeduel/index.docbook
/usr/share/doc/HTML/de/ksnakeduel/settings-general.png
/usr/share/doc/HTML/de/ksnakeduel/settings-theme.png
/usr/share/doc/HTML/en/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/en/ksnakeduel/index.docbook
/usr/share/doc/HTML/en/ksnakeduel/settings-general.png
/usr/share/doc/HTML/en/ksnakeduel/settings-theme.png
/usr/share/doc/HTML/es/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/es/ksnakeduel/index.docbook
/usr/share/doc/HTML/et/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/et/ksnakeduel/index.docbook
/usr/share/doc/HTML/fr/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/fr/ksnakeduel/index.docbook
/usr/share/doc/HTML/fr/ksnakeduel/settings-general.png
/usr/share/doc/HTML/fr/ksnakeduel/settings-theme.png
/usr/share/doc/HTML/it/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/it/ksnakeduel/index.docbook
/usr/share/doc/HTML/nl/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/nl/ksnakeduel/index.docbook
/usr/share/doc/HTML/pt/ksnakeduel/index.cache.bz2
/usr/share/doc/HTML/pt/ksnakeduel/index.docbook
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
/usr/share/package-licenses/ksnakeduel/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/ksnakeduel/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f ksnakeduel.lang
%defattr(-,root,root,-)

