RELEASE ?= R4.1

BASE_DIRS = backgrounds icons
ANACONDA_DIRS = anaconda firstboot/qubes
EFI_DIRS = bootloader/apple
PLYMOUTH_DIRS = plymouth

DIRS = $(BASE_DIRS) $(ANACONDA_DIRS) $(EFI_DIRS) $(PLYMOUTH_DIRS)

.PHONY: all
all:
	@for dir in $(DIRS); do $(MAKE) -C $$dir RELEASE=$(RELEASE) $@ || exit 1; done

.PHONY: clean
clean:
	@for dir in $(DIRS); do $(MAKE) -C $$dir $@ || exit 1; done

install-base:
	install -d $(DESTDIR)
	@for dir in $(BASE_DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) install || exit 1; done

install-anaconda:
	install -d $(DESTDIR)
	@for dir in $(ANACONDA_DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) install || exit 1; done

install-efi:
	install -D -m 0644 anaconda/syslinux-splash.png \
		$(DESTDIR)/boot/efi/EFI/qubes/splash.png
	install -D -m 0644 plymouth/qubes-dark/qubes-logo-solid.png \
		$(DESTDIR)/boot/efi/EFI/qubes/icons/os_qubes.png
	install -d $(DESTDIR)
	@for dir in $(EFI_DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) install || exit 1; done

install-plymouth:
	install -d $(DESTDIR)
	@for dir in $(PLYMOUTH_DIRS); do $(MAKE) -C $$dir DESTDIR=$(DESTDIR) install || exit 1; done

install: install-base install-anaconda install-efi install-plymouth