setup:
	tlmgr init-usertree
	sudo tlmgr option repository ftp://tug.org/historic/systems/texlive/2017/tlnet-final
	tlmgr install scquotes hyperref xcolor pagecolor afterpage graphicx

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

play:
	audacity source/*.mp4

clean:
	rm build -rf