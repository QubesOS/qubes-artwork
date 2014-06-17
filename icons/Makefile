DIRS = $(wildcard *x*) scalable

all:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: all

clean:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
.PHONY: clean

install:
	for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@ || exit 1; done
.PHONY: install
