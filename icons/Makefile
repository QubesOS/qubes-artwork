DIRS = $(wildcard *x*) scalable

all:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: all

clean:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: clean

install:
	for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@ || exit 1; done
	for size in 16x16 32x32 48x48 64x64; do \
		mkdir -p $(DESTDIR)/usr/share/icons/oxygen/$${size}/places; \
		ln -s ../../../hicolor/$${size}/places/start-here-qubes-blue.png $(DESTDIR)/usr/share/icons/oxygen/$${size}/places/start-here-qubes.png; \
		ln -s ../../../hicolor/$${size}/places/start-here-qubes-blue.png $(DESTDIR)/usr/share/icons/oxygen/$${size}/places/start-here-qubes-blue.png; \
		ln -s ../../../hicolor/$${size}/places/start-here-qubes-green.png $(DESTDIR)/usr/share/icons/oxygen/$${size}/places/start-here-qubes-green.png; \
		ln -s ../../../hicolor/$${size}/places/start-here-qubes-red.png $(DESTDIR)/usr/share/icons/oxygen/$${size}/places/start-here-qubes-red.png; \
		ln -s ../../../hicolor/$${size}/places/start-here-qubes-yellow.png $(DESTDIR)/usr/share/icons/oxygen/$${size}/places/start-here-qubes-yellow.png; \
	done
	mkdir -p $(DESTDIR)/usr/share/icons/oxygen/scalable/places/
	ln -s ../../../hicolor/scalable/places/start-here-qubes-blue.svg $(DESTDIR)/usr/share/icons/oxygen/scalable/places/start-here-qubes.svg
	ln -s ../../../hicolor/scalable/places/start-here-qubes-blue.svg $(DESTDIR)/usr/share/icons/oxygen/scalable/places/start-here-qubes-blue.svg
	ln -s ../../../hicolor/scalable/places/start-here-qubes-green.svg $(DESTDIR)/usr/share/icons/oxygen/scalable/places/start-here-qubes-green.svg
	ln -s ../../../hicolor/scalable/places/start-here-qubes-red.svg $(DESTDIR)/usr/share/icons/oxygen/scalable/places/start-here-qubes-red.svg
	ln -s ../../../hicolor/scalable/places/start-here-qubes-yellow.svg $(DESTDIR)/usr/share/icons/oxygen/scalable/places/start-here-qubes-yellow.svg

	mkdir -p $(DESTDIR)/usr/share/icons/hicolor/scalable/apps/
	cp scalable/apps/* $(DESTDIR)/usr/share/icons/hicolor/scalable/apps/
.PHONY: install
