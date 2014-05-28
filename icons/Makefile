DIRS = $(wildcard *x*) scalable

all:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@; done
.PHONY: all

clean:
	for dir in $(DIRS); do $(MAKE) -C $$dir $@; done
.PHONY: clean

install:
	for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@; done
.PHONY: install
