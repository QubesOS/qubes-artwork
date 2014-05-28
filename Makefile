VERSION = 1
RELEASE ?= R2-rc1

DIRS = \
	anaconda \
	backgrounds \
	grub \
	icons \
	firstboot/qubes \
	plymouth/qubes-dark \
	src/qubes

RPMDIR = rpm/

all:
	@for dir in $(DIRS); do $(MAKE) -C $$dir RELEASE=$(RELEASE) $@; done
.PHONY: all

clean:
	@for dir in $(DIRS); do $(MAKE) -C $$dir $@; done
	$(RM) -r $(RPMDIR) *.list
.PHONY: clean

install:
	install -d $(DESTDIR)
	@for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@; done
.PHONY: install

rpms:
	rpmbuild --define "_rpmdir $(RPMDIR)" --define "version $(VERSION)" -bb qubes-artwork.spec
#	rpm --addsign $(RPMDIR)/x86_64/qubes-artwork-*$(VERSION)*.rpm
.PHONY: rpms
