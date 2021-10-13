.PHONY: all clean
all: anki-import-scheduling-info-from-csv.ankiaddon
anki-import-scheduling-info-from-csv.ankiaddon:
	zip -r $@ $$(git ls-files | grep -v ^Makefile$$)
clean:
	rm -f anki-import-scheduling-info-from-csv.ankiaddon
