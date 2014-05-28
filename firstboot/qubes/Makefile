ALL = splash-small.png

all: $(ALL)
.PHONY: all

splash-small.png: GEOMETRY = 128x128
%.png: %.svg
	convert -background none -geometry $(GEOMETRY) $< $@

clean:
	$(RM) $(ALL)
.PHONY: clean

install:
	mkdir -p $(DESTDIR)/usr/share/firstboot/themes/qubes
	install -m 0644 -t $(DESTDIR)/usr/share/firstboot/themes/qubes \
		$(ALL) \
		firstboot-left.png \
		workstation.png
.PHONY: install
