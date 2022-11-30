RELEASE ?= PRERELEASE
ALL = \
	progress_first.png \
	progress_first-lowres.png \
	splash.png \
	syslinux-vesa-splash.jpg \

all: $(ALL) syslinux-splash.png
.PHONY: all

splash.png: GEOMETRY = 128x128
%.png: %.svg
	gm convert -background none -geometry $(GEOMETRY) $< $@

syslinux-vesa-splash.jpg: splash.svg
	gm convert splash.svg $@

syslinux-splash.png: syslinux-splash.svg
	gm convert $< -colors 12 -geometry "640x480!" $@

# this part requires syslinux-perl
# (not in BuildRequires, but are we using syslinux?)
syslinux-splash.pnm: syslinux-splash.rel.svg
	gm convert $< -colors 12 $@

splash.lss: syslinux-splash.pnm
	ppmtolss16 '#000000=0' '#ffffff=1' '#cdcfd5=7' '#c90000=15' < $< > $@

# FIXME those appear to work, but violate rules specified in README
progress_first.png: splash.png
	cp $< $@
progress_first-lowres.png: splash.png
	cp $< $@

clean:
	$(RM) $(ALL) syslinux-splash.{pnm,png} splash.lss *.rel.svg
.PHONY: clean

install:
	mkdir -p $(DESTDIR)/usr/share/anaconda/boot
	install -m 0644 -t $(DESTDIR)/usr/share/anaconda/boot \
		syslinux-splash.png
	mkdir -p $(DESTDIR)/usr/share/anaconda/pixmaps
	install -m 0644 -t $(DESTDIR)/usr/share/anaconda/pixmaps \
		$(ALL) \
		anaconda_header.png \
		sidebar-bg.png \
		sidebar-logo.png \
		topbar-bg.png

.PHONY: install
