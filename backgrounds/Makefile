RELEASE ?= PRERELEASE
ALLSVG = $(patsubst %.in.svg,%.svg,$(wildcard *.in.svg))

AUTHOR = Michał Kopczyński
LICENCE = CC-BY-SA 4.0
KDEGEOMETRIES = 1920x1080 1600x900

all: $(ALLSVG) kde
.PHONY: all

%.rel.svg: %.in.svg
	sed -e 's|@@RELEASE@@|$(RELEASE)|' $< > $@

# Inkscape 0.48.x cannot outline text when exporting to plain SVG without GUI.
# The bug is fixed in trunk: https://bugs.launchpad.net/inkscape/+bug/903772.
#
# https://stackoverflow.com/questions/8422558/converting-text-into-path-svg-on-server
# does not appear to work on fc20.
%.svg: %.rel.svg
	cp $< $@
#	inkscape --export-plain-svg=$@ --export-text-to-path $<

kde: $(ALLSVG)
	mkdir -p $@
	for svg in $(ALLSVG); do \
		../bin/mkkdewallpaper.sh $@ $$svg "$(AUTHOR)" "$(LICENCE)" $(KDEGEOMETRIES) || exit 1; \
	done

clean:
	$(RM) $(ALLSVG) *.rel.svg
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

.PHONY: install
