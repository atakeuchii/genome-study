.PHONY: build serve commit

build:
	python3 build.py

serve: build
	@echo "http://localhost:8000 で確認 (Ctrl-C で終了)"
	python3 -m http.server 8000

commit: build
	git add -A
	git commit -m "Update study notes"
	git push
