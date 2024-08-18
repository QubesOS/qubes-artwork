DIRS = qubes-dark

all:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: all

clean:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: clean

install:
	for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@ || exit 1; done
	mkdir -p $(DESTDIR)/usr/lib/dracut/dracut.conf.d/
	cp plymouth-missing-fonts.conf $(DESTDIR)/usr/lib/dracut/dracut.conf.d/
.PHONY: install
