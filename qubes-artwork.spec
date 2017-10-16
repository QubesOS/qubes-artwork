
%global debug_package %{nil}
%{!?version: %define version %(cat version)}

Name:		qubes-artwork
Version:	%{version}
Release:	2%{?dist}

Summary:	Qubes branding
License:	CC BY-SA 4.0 International, GPL v2
Group:		Qubes
Vendor:		Invisible Things Lab
URL:		https://www.qubes-os.org
BuildArch:	noarch

Provides:	system-logos
Provides:	redhat-logos
Provides:	fedora-logos
Provides:	qubes-logos
Provides:	desktop-backgrounds-compat
Obsoletes:	redhat-logos
Obsoletes:	fedora-logos
Obsoletes:	qubes-logos
Obsoletes:	desktop-backgrounds-compat

Requires(post):	plymouth
Requires(post):	plymouth-scripts
# plymouth-scripts should depend on plymouth-plugin-scripts, but it does not
Requires(post):	plymouth-plugin-script
Requires(post):	plymouth-plugin-label
Requires(post):	dracut

BuildRequires:	ImageMagick
BuildRequires:	google-roboto-fonts
%if 0%{?rhel} >= 7
BuildRequires:	python34-qubesimgconverter
%else
BuildRequires:	python3-qubesimgconverter
%endif
BuildRequires:	netpbm-progs
BuildRequires:	pycairo

# see backgrounds/Makefile
#BuildRequires:	inkscape >= 0.91

%define _builddir %(pwd)

%description
Qubes-branded backgrounds, icons, themes.

%package efi
Summary:    Qubes OS theme for EFI boot manager (rEFInd)

%description efi
Qubes OS theme for rEFInd boot manager

%prep
rm -rf %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D
make clean
mkdir -p %{_rpmdir}

%build
make


%install
make install DESTDIR=%{buildroot}

%post
/usr/sbin/plymouth-set-default-theme qubes-dark && \
PATH="/sbin:$PATH" dracut -f || :
xdg-icon-resource forceupdate --theme hicolor || :
xdg-icon-resource forceupdate --theme oxygen || :

#
# triggers
#

%triggerin -- plymouth
/usr/sbin/plymouth-set-default-theme qubes-dark || :

#
# files -- please keep them sorted
#

%files
# docs
%doc COPYING
%doc HACKING

# icons
%{_datadir}/icons/hicolor/16x16/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/16x16/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/16x16/apps/qubes-manager.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-black.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-blue.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-gray.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-green.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-orange.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-purple.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-red.png
%{_datadir}/icons/hicolor/16x16/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-black.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-green.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-red.png
%{_datadir}/icons/hicolor/16x16/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/16x16/places/start-here-qubes-blue.png
%{_datadir}/icons/hicolor/16x16/places/start-here-qubes-green.png
%{_datadir}/icons/hicolor/16x16/places/start-here-qubes-red.png
%{_datadir}/icons/hicolor/16x16/places/start-here-qubes-yellow.png
%{_datadir}/icons/hicolor/22x22/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/22x22/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/22x22/apps/qubes-manager.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-black.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-blue.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-gray.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-green.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-orange.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-purple.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-red.png
%{_datadir}/icons/hicolor/22x22/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-black.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-green.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-red.png
%{_datadir}/icons/hicolor/22x22/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/24x24/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/24x24/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/24x24/apps/qubes-manager.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-black.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-blue.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-gray.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-green.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-orange.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-purple.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-red.png
%{_datadir}/icons/hicolor/24x24/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-black.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-green.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-red.png
%{_datadir}/icons/hicolor/24x24/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-manager.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-black.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-blue.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-gray.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-green.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-orange.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-purple.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-red.png
%{_datadir}/icons/hicolor/32x32/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-black.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-green.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-red.png
%{_datadir}/icons/hicolor/32x32/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/32x32/places/start-here-qubes-blue.png
%{_datadir}/icons/hicolor/32x32/places/start-here-qubes-green.png
%{_datadir}/icons/hicolor/32x32/places/start-here-qubes-red.png
%{_datadir}/icons/hicolor/32x32/places/start-here-qubes-yellow.png
%{_datadir}/icons/hicolor/36x36/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/36x36/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/36x36/apps/qubes-manager.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-black.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-blue.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-gray.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-green.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-orange.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-purple.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-red.png
%{_datadir}/icons/hicolor/36x36/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-black.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-green.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-red.png
%{_datadir}/icons/hicolor/36x36/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-manager.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-black.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-blue.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-gray.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-green.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-orange.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-purple.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-red.png
%{_datadir}/icons/hicolor/48x48/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-black.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-green.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-red.png
%{_datadir}/icons/hicolor/48x48/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/48x48/places/start-here-qubes-blue.png
%{_datadir}/icons/hicolor/48x48/places/start-here-qubes-green.png
%{_datadir}/icons/hicolor/48x48/places/start-here-qubes-red.png
%{_datadir}/icons/hicolor/48x48/places/start-here-qubes-yellow.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-manager.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-black.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-blue.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-gray.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-green.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-orange.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-purple.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-red.png
%{_datadir}/icons/hicolor/64x64/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-black.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-green.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-red.png
%{_datadir}/icons/hicolor/64x64/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/64x64/places/start-here-qubes-blue.png
%{_datadir}/icons/hicolor/64x64/places/start-here-qubes-green.png
%{_datadir}/icons/hicolor/64x64/places/start-here-qubes-red.png
%{_datadir}/icons/hicolor/64x64/places/start-here-qubes-yellow.png
%{_datadir}/icons/hicolor/72x72/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/72x72/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/72x72/apps/qubes-manager.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-black.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-blue.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-gray.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-green.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-orange.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-purple.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-red.png
%{_datadir}/icons/hicolor/72x72/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-black.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-green.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-red.png
%{_datadir}/icons/hicolor/72x72/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/96x96/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/96x96/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/96x96/apps/qubes-manager.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-black.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-blue.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-gray.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-green.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-orange.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-purple.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-red.png
%{_datadir}/icons/hicolor/96x96/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-black.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-green.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-red.png
%{_datadir}/icons/hicolor/96x96/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/128x128/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/128x128/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/128x128/apps/qubes-manager.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-black.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-blue.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-gray.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-green.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-orange.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-purple.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-red.png
%{_datadir}/icons/hicolor/128x128/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-black.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-green.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-red.png
%{_datadir}/icons/hicolor/128x128/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/192x192/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/192x192/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/192x192/apps/qubes-manager.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-black.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-blue.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-gray.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-green.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-orange.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-purple.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-red.png
%{_datadir}/icons/hicolor/192x192/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-black.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-green.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-red.png
%{_datadir}/icons/hicolor/192x192/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/256x256/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/256x256/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/256x256/apps/qubes-manager.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-black.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-blue.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-gray.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-green.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-orange.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-purple.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-red.png
%{_datadir}/icons/hicolor/256x256/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-black.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-green.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-red.png
%{_datadir}/icons/hicolor/256x256/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/512x512/apps/qubes-appmenu-select.png
%{_datadir}/icons/hicolor/512x512/apps/qubes-logo-icon.png
%{_datadir}/icons/hicolor/512x512/apps/qubes-manager.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-black.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-blue.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-gray.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-green.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-orange.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-purple.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-red.png
%{_datadir}/icons/hicolor/512x512/devices/appvm-yellow.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-black.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-blue.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-gray.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-green.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-orange.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-purple.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-red.png
%{_datadir}/icons/hicolor/512x512/devices/dispvm-yellow.png
%{_datadir}/icons/hicolor/scalable/places/start-here-qubes-blue.svg
%{_datadir}/icons/hicolor/scalable/places/start-here-qubes-green.svg
%{_datadir}/icons/hicolor/scalable/places/start-here-qubes-red.svg
%{_datadir}/icons/hicolor/scalable/places/start-here-qubes-yellow.svg
%{_datadir}/icons/oxygen/16x16/places/start-here-qubes.png
%{_datadir}/icons/oxygen/16x16/places/start-here-qubes-blue.png
%{_datadir}/icons/oxygen/16x16/places/start-here-qubes-green.png
%{_datadir}/icons/oxygen/16x16/places/start-here-qubes-red.png
%{_datadir}/icons/oxygen/16x16/places/start-here-qubes-yellow.png
%{_datadir}/icons/oxygen/32x32/places/start-here-qubes.png
%{_datadir}/icons/oxygen/32x32/places/start-here-qubes-blue.png
%{_datadir}/icons/oxygen/32x32/places/start-here-qubes-green.png
%{_datadir}/icons/oxygen/32x32/places/start-here-qubes-red.png
%{_datadir}/icons/oxygen/32x32/places/start-here-qubes-yellow.png
%{_datadir}/icons/oxygen/48x48/places/start-here-qubes.png
%{_datadir}/icons/oxygen/48x48/places/start-here-qubes-blue.png
%{_datadir}/icons/oxygen/48x48/places/start-here-qubes-green.png
%{_datadir}/icons/oxygen/48x48/places/start-here-qubes-red.png
%{_datadir}/icons/oxygen/48x48/places/start-here-qubes-yellow.png
%{_datadir}/icons/oxygen/64x64/places/start-here-qubes.png
%{_datadir}/icons/oxygen/64x64/places/start-here-qubes-blue.png
%{_datadir}/icons/oxygen/64x64/places/start-here-qubes-green.png
%{_datadir}/icons/oxygen/64x64/places/start-here-qubes-red.png
%{_datadir}/icons/oxygen/64x64/places/start-here-qubes-yellow.png
%{_datadir}/icons/oxygen/scalable/places/start-here-qubes.svg
%{_datadir}/icons/oxygen/scalable/places/start-here-qubes-blue.svg
%{_datadir}/icons/oxygen/scalable/places/start-here-qubes-green.svg
%{_datadir}/icons/oxygen/scalable/places/start-here-qubes-red.svg
%{_datadir}/icons/oxygen/scalable/places/start-here-qubes-yellow.svg

# backgrounds
%{_datadir}/backgrounds/qubes/qubes-blackcurrant.svg
%{_datadir}/backgrounds/qubes/qubes-chemtrail.svg
%{_datadir}/backgrounds/qubes/qubes-dawn.svg
%{_datadir}/backgrounds/qubes/qubes-grass.svg
%{_datadir}/backgrounds/qubes/qubes-honey.svg
%{_datadir}/backgrounds/qubes/qubes-paper.svg
%{_datadir}/backgrounds/qubes/qubes-plum.svg
%{_datadir}/backgrounds/qubes/qubes-poison.svg
%{_datadir}/backgrounds/qubes/qubes-salmon.svg
%{_datadir}/backgrounds/qubes/qubes-sea.svg
%{_datadir}/backgrounds/qubes/qubes-sky.svg
%{_datadir}/backgrounds/qubes/qubes-smoke.svg
%{_datadir}/backgrounds/qubes/qubes-steel.svg
%{_datadir}/backgrounds/qubes/qubes-sun.svg
%{_datadir}/backgrounds/qubes/qubes-swamp.svg
%{_datadir}/backgrounds/qubes/qubes-wasp.svg
%{_datadir}/backgrounds/qubes/qubes-wild-strawberry.svg
%{_datadir}/backgrounds/qubes/qubes-wine.svg

%{_datadir}/backgrounds/xfce/qubes-blackcurrant.svg
%{_datadir}/backgrounds/xfce/qubes-chemtrail.svg
%{_datadir}/backgrounds/xfce/qubes-dawn.svg
%{_datadir}/backgrounds/xfce/qubes-grass.svg
%{_datadir}/backgrounds/xfce/qubes-honey.svg
%{_datadir}/backgrounds/xfce/qubes-paper.svg
%{_datadir}/backgrounds/xfce/qubes-plum.svg
%{_datadir}/backgrounds/xfce/qubes-poison.svg
%{_datadir}/backgrounds/xfce/qubes-salmon.svg
%{_datadir}/backgrounds/xfce/qubes-sea.svg
%{_datadir}/backgrounds/xfce/qubes-sky.svg
%{_datadir}/backgrounds/xfce/qubes-smoke.svg
%{_datadir}/backgrounds/xfce/qubes-steel.svg
%{_datadir}/backgrounds/xfce/qubes-sun.svg
%{_datadir}/backgrounds/xfce/qubes-swamp.svg
%{_datadir}/backgrounds/xfce/qubes-wasp.svg
%{_datadir}/backgrounds/xfce/qubes-wild-strawberry.svg
%{_datadir}/backgrounds/xfce/qubes-wine.svg

%{_datadir}/backgrounds/default.png
%{_datadir}/backgrounds/images/default.png

%{_datadir}/wallpapers/Qubes_Blackcurrant/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Blackcurrant/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Blackcurrant/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Blackcurrant/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Blackcurrant/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Blackcurrant/metadata.desktop
%{_datadir}/wallpapers/Qubes_Chemtrail/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Chemtrail/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Chemtrail/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Chemtrail/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Chemtrail/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Chemtrail/metadata.desktop
%{_datadir}/wallpapers/Qubes_Dawn/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Dawn/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Dawn/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Dawn/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Dawn/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Dawn/metadata.desktop
%{_datadir}/wallpapers/Qubes_Grass/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Grass/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Grass/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Grass/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Grass/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Grass/metadata.desktop
%{_datadir}/wallpapers/Qubes_Honey/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Honey/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Honey/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Honey/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Honey/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Honey/metadata.desktop
%{_datadir}/wallpapers/Qubes_Paper/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Paper/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Paper/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Paper/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Paper/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Paper/metadata.desktop
%{_datadir}/wallpapers/Qubes_Plum/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Plum/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Plum/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Plum/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Plum/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Plum/metadata.desktop
%{_datadir}/wallpapers/Qubes_Poison/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Poison/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Poison/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Poison/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Poison/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Poison/metadata.desktop
%{_datadir}/wallpapers/Qubes_Salmon/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Salmon/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Salmon/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Salmon/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Salmon/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Salmon/metadata.desktop
%{_datadir}/wallpapers/Qubes_Sea/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Sea/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Sea/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Sea/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Sea/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Sea/metadata.desktop
%{_datadir}/wallpapers/Qubes_Sky/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Sky/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Sky/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Sky/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Sky/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Sky/metadata.desktop
%{_datadir}/wallpapers/Qubes_Smoke/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Smoke/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Smoke/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Smoke/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Smoke/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Smoke/metadata.desktop
%{_datadir}/wallpapers/Qubes_Steel/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Steel/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Steel/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Steel/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Steel/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Steel/metadata.desktop
%{_datadir}/wallpapers/Qubes_Sun/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Sun/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Sun/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Sun/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Sun/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Sun/metadata.desktop
%{_datadir}/wallpapers/Qubes_Swamp/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Swamp/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Swamp/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Swamp/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Swamp/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Swamp/metadata.desktop
%{_datadir}/wallpapers/Qubes_Wasp/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Wasp/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Wasp/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Wasp/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Wasp/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Wasp/metadata.desktop
%{_datadir}/wallpapers/Qubes_Wild_Strawberry/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Wild_Strawberry/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Wild_Strawberry/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Wild_Strawberry/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Wild_Strawberry/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Wild_Strawberry/metadata.desktop
%{_datadir}/wallpapers/Qubes_Wine/contents/images/1280x1024.png
%{_datadir}/wallpapers/Qubes_Wine/contents/images/1600x900.png
%{_datadir}/wallpapers/Qubes_Wine/contents/images/1920x1080.png
%{_datadir}/wallpapers/Qubes_Wine/contents/images/2048x1536.png
%{_datadir}/wallpapers/Qubes_Wine/contents/screenshot.png
%{_datadir}/wallpapers/Qubes_Wine/metadata.desktop

# anaconda
%{_datadir}/anaconda/boot/syslinux-splash.png
%{_datadir}/anaconda/pixmaps/anaconda_header.png
%{_datadir}/anaconda/pixmaps/progress_first-lowres.png
%{_datadir}/anaconda/pixmaps/progress_first.png
%{_datadir}/anaconda/pixmaps/sidebar-bg.png
%{_datadir}/anaconda/pixmaps/sidebar-logo.png
%{_datadir}/anaconda/pixmaps/splash.png
%{_datadir}/anaconda/pixmaps/syslinux-vesa-splash.jpg
%{_datadir}/anaconda/pixmaps/topbar-bg.png

# firstboot
%{_datadir}/firstboot/themes/qubes/firstboot-left.png
%{_datadir}/firstboot/themes/qubes/splash-small.png
%{_datadir}/firstboot/themes/qubes/workstation.png

# plymouth
%{_sysconfdir}/dracut.conf.d/plymouth-missing-fonts.conf
%{_datadir}/plymouth/themes/qubes-dark/bullet.png
%{_datadir}/plymouth/themes/qubes-dark/entry.png
%{_datadir}/plymouth/themes/qubes-dark/padlock.png
%{_datadir}/plymouth/themes/qubes-dark/progress_bar.png
%{_datadir}/plymouth/themes/qubes-dark/progress_box.png
%{_datadir}/plymouth/themes/qubes-dark/qubes-dark.plymouth
%{_datadir}/plymouth/themes/qubes-dark/qubes-dark.script
%{_datadir}/plymouth/themes/qubes-dark/qubes-logo-outline.png
%{_datadir}/plymouth/themes/qubes-dark/qubes-logo-solid.png

# misc files
/boot/grub/splash.xpm.gz
/boot/grub2/themes/system/fireworks.png

%files efi
/boot/efi/EFI/qubes/splash.png
/boot/efi/EFI/qubes/icons/os_qubes.png

%changelog

