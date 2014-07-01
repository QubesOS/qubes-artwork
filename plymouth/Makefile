DIRS = qubes-dark

all:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: all

clean:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: clean

install:
	for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@ || exit 1; done
	mkdir -p $(DESTDIR)/etc/dracut.conf.d/
	cp plymouth-missing-fonts.conf $(DESTDIR)/etc/dracut.conf.d/
.PHONY: install
