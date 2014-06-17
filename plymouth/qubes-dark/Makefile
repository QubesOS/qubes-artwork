ALL = $(patsubst %.svg,%.png,$(wildcard *.svg)) padlock.png

all: $(ALL)
.PHONY: all

%.png: %.svg
	convert -background none -antialias $< $@
#	inkscape --export-png=$@ $<

padlock.png:
	../../bin/mkpadlock.py -s 40 -c 0xcc0000 $@

clean:
	$(RM) $(ALL)
.PHONY: clean

install:
	mkdir -p $(DESTDIR)/usr/share/plymouth/themes/qubes-dark
	install -m 0644 -t $(DESTDIR)/usr/share/plymouth/themes/qubes-dark \
		$(ALL) \
		bullet.png \
		entry.png \
		progress_bar.png \
		progress_box.png \
		qubes-dark.plymouth \
		qubes-dark.script

.PHONY: install
