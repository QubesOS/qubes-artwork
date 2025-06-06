AUTHOR = Michał Kopczyński
LICENCE = CC-BY-SA 4.0
ALLSVG = $(wildcard *.svg)
ALLJPG = $(wildcard *.jpg)
KDEGEOMETRIES = \
	7680x4320 \
	3840x2160 \
	3440x1440 \
	2880x1920 \
	2560x1440 \
	2560x1080 \
	2256x1504 \
	1920x1200 \
	1920x1080 \
	1600x900  \
	1366x768  \
	1280x1024 \
	1280x720

all: kde
.PHONY: all

kde: $(ALLSVG)
	mkdir -p $@
	for svg in $(ALLSVG); do \
		../bin/mkkdewallpaper.sh $@ $$svg "$(AUTHOR)" "$(LICENCE)" $(KDEGEOMETRIES) || exit 1; \
	done

clean:
	$(RM) -r kde
.PHONY: clean

install:
	install -d $(DESTDIR)/usr/share/backgrounds/qubes
	install -t $(DESTDIR)/usr/share/backgrounds/qubes -m 644 $(ALLSVG)
	install -t $(DESTDIR)/usr/share/backgrounds/qubes -m 644 $(ALLJPG)

	install -d $(DESTDIR)/usr/share/backgrounds/images
	for svg in $(notdir $(ALLSVG)); do \
		ln -s ../qubes/$$svg $(DESTDIR)/usr/share/backgrounds/images/ || exit 1; \
	done
	for jpg in $(notdir $(ALLJPG)); do \
		ln -s ../qubes/$$jpg $(DESTDIR)/usr/share/backgrounds/images/ || exit 1; \
	done

	install -d $(DESTDIR)/usr/share/wallpapers
	cp -r kde/* $(DESTDIR)/usr/share/wallpapers

	install -d $(DESTDIR)/usr/share/backgrounds/images
	ln -s ../wallpapers/Qubes_Steel/contents/images/1920x1080.png $(DESTDIR)/usr/share/backgrounds/default.png
	ln -s ../../wallpapers/Qubes_Steel/contents/images/1920x1080.png $(DESTDIR)/usr/share/backgrounds/images/default.png
	gm convert $(DESTDIR)/usr/share/backgrounds/images/default.png \
		$(DESTDIR)/usr/share/backgrounds/images/default.webp
	gm convert $(DESTDIR)/usr/share/backgrounds/images/default.png \
		$(DESTDIR)/usr/share/backgrounds/images/default.jxl

.PHONY: install
