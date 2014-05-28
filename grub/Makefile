RELEASE ?= PRERELEASE
ALL = $(patsubst %.in.svg,%.xpm.gz,$(wildcard *.in.svg))

all: $(ALL)
.PHONY: all

%.rel.svg: %.in.svg
	sed -e 's|@@RELEASE@@|$(RELEASE)|' $< > $@

%.xpm.gz: %.rel.svg
	convert $< $@

clean:
	$(RM) $(ALL) *.rel.svg
.PHONY: clean

install:
	install -d $(DESTDIR)/boot/grub
	install -t $(DESTDIR)/boot/grub -m 644 $(ALL)
.PHONY: install
