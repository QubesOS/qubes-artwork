AUTHOR = Michał Kopczyński
LICENCE = CC-BY-SA 4.0
KDEGEOMETRIES = 2048x1536 1920x1080 1600x900 1280x1024
ALLSVG = $(wildcard *.svg)

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

	install -d $(DESTDIR)/usr/share/backgrounds/xfce
	for svg in $(notdir $(ALLSVG)); do \
		ln -s ../qubes/$$svg $(DESTDIR)/usr/share/backgrounds/xfce/ || exit 1; \
	done

	install -d $(DESTDIR)/usr/share/wallpapers
	cp -r kde/* $(DESTDIR)/usr/share/wallpapers

	install -d $(DESTDIR)/usr/share/backgrounds/images
	ln -s ../wallpapers/Qubes_Steel/contents/images/2048x1536.png $(DESTDIR)/usr/share/backgrounds/default.png
	ln -s ../../wallpapers/Qubes_Steel/contents/images/2048x1536.png $(DESTDIR)/usr/share/backgrounds/images/default.png

.PHONY: install
