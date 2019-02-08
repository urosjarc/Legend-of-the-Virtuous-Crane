book: clean
	cp ./latex ./build -r
	rm ./build/book -rf
	cp latex/book/$(LANG) build/book -r

	cd build && pdflatex main.tex
	xdg-open build/main.pdf

book-sl:
	$(MAKE) book LANG=slovenian

book-en:
	$(MAKE) book LANG=english

clean:
	rm build -rf