Name:		qubes-artwork
Version:	1
Release:	1%{?dist}

Summary:	Qubes branding
License:	CC BY-SA 4.0 International, GPL v2
Group:		Qubes
Vendor:		Invisible Things Lab
URL:		https://www.qubes-os.org

Provides:	system-logos
Provides:	redhat-logos
Provides:	fedora-logos
Provides:	desktop-backgrounds-compat
Obsoletes:	redhat-logos
Obsoletes:	fedora-logos
Obsoletes:	desktop-backgrounds-compat

Requires(post):	plymouth-scripts
# plymouth-scripts should depend on plymouth-plugin-scripts, but it does not
Requires(post):	plymouth-plugin-script

BuildRequires:	ImageMagick
BuildRequires:	google-roboto-fonts
BuildRequires:	qubes-utils >= 2.0.10
BuildRequires:	netpbm-progs

# see backgrounds/Makefile
#BuildRequires:	inkscape >= 0.91

%define _builddir %(pwd)
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description
Qubes-branded backgrounds, icons, themes.

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
/usr/sbin/plymouth-set-default-theme qubes-dark || :

#
# triggers
#

%triggerin -- plymouth
cp -f %{_datadir}/plymouth/plymouthd.defaults.qubes %{_datadir}/plymouth/plymouthd.defaults
/usr/sbin/plymouth-set-default-theme qubes-dark || :

#
# files -- please keep them sorted
#

%files
# docs
%doc COPYING
%doc HACKING

# icons
%{_datadir}/icons/hicolor/16x16/apps/qubes-manager.png
%{_datadir}/icons/hicolor/16x16/apps/qubes-menu-icon-blue.png
%{_datadir}/icons/hicolor/16x16/apps/qubes-menu-icon-green.png
%{_datadir}/icons/hicolor/16x16/apps/qubes-menu-icon-red.png
%{_datadir}/icons/hicolor/16x16/apps/qubes-menu-icon-yellow.png
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
%{_datadir}/icons/hicolor/32x32/apps/qubes-manager.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-menu-icon-blue.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-menu-icon-green.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-menu-icon-red.png
%{_datadir}/icons/hicolor/32x32/apps/qubes-menu-icon-yellow.png
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
%{_datadir}/icons/hicolor/48x48/apps/qubes-manager.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-menu-icon-blue.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-menu-icon-green.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-menu-icon-red.png
%{_datadir}/icons/hicolor/48x48/apps/qubes-menu-icon-yellow.png
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
%{_datadir}/icons/hicolor/64x64/apps/qubes-manager.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-menu-icon-blue.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-menu-icon-green.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-menu-icon-red.png
%{_datadir}/icons/hicolor/64x64/apps/qubes-menu-icon-yellow.png
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
%{_datadir}/icons/hicolor/scalable/apps/qubes-menu-icon-blue.svg
%{_datadir}/icons/hicolor/scalable/apps/qubes-menu-icon-green.svg
%{_datadir}/icons/hicolor/scalable/apps/qubes-menu-icon-red.svg
%{_datadir}/icons/hicolor/scalable/apps/qubes-menu-icon-yellow.svg

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
%{_datadir}/anaconda/pixmaps/splash.png
%{_datadir}/anaconda/pixmaps/syslinux-vesa-splash.jpg

# firstboot
%{_datadir}/firstboot/themes/qubes/firstboot-left.png
%{_datadir}/firstboot/themes/qubes/splash-small.png
%{_datadir}/firstboot/themes/qubes/workstation.png

# plymouth
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

# python modules
%{python_sitearch}/qubes/imggen.py
%{python_sitearch}/qubes/imggen.pyc
%{python_sitearch}/qubes/imggen.pyo


%changelog

