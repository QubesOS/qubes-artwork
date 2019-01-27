RELEASE ?= R2-rc1

DIRS = \
	anaconda \
	backgrounds \
	bootloader/apple \
	icons \
	firstboot/qubes \
	plymouth

RPMDIR = rpm/

all:
	@for dir in $(DIRS); do $(MAKE) -C $$dir RELEASE=$(RELEASE) $@ || exit 1; done
.PHONY: all

clean:
	@for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done
	$(RM) -r $(RPMDIR) *.list
.PHONY: clean

install:
	install -d $(DESTDIR)
	@for dir in $(DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) $@ || exit 1; done
	@# temporary theme
	install -D -m 0644 anaconda/syslinux-splash.png \
		$(DESTDIR)/boot/efi/EFI/qubes/splash.png
	install -D -m 0644 plymouth/qubes-dark/qubes-logo-solid.png \
		$(DESTDIR)/boot/efi/EFI/qubes/icons/os_qubes.png

.PHONY: install


rpms:
	rpmbuild --define "_rpmdir $(RPMDIR)" -bb qubes-artwork.spec
#	rpm --addsign $(RPMDIR)/x86_64/qubes-artwork-*$(VERSION)*.rpm
.PHONY: rpms
