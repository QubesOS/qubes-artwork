RELEASE ?= PRERELEASE
ALL = splash.xpm.gz fireworks.png

all: $(ALL)
.PHONY: all

$(ALL): splash.svg
	convert $< $@

clean:
	$(RM) $(ALL)
.PHONY: clean

install:
	install -d $(DESTDIR)/boot/grub
	install -t $(DESTDIR)/boot/grub -m 644 splash.xpm.gz

	install -d $(DESTDIR)/boot/grub2/themes/system
	install -t $(DESTDIR)/boot/grub2/themes/system/ -m 644 fireworks.png
.PHONY: install
