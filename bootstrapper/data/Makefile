# Makefile for FIRST Tech Challenge Documentation {{translation.language}} Translation
#
# Here is what you can do:
#
# - make  # Automatically build an HTML local version
# - make todo  # To list remaining tasks and show current progression
# - make verifs  # To check for correctness: wrapping, spelling
# - make wrap  # To rewrap modified files
# - make spell  # To check for spelling
# - make clean # To remove build artifacts
# - make fuzzy  # To find fuzzy strings

# Configuration

# The FTCDOCS_CURRENT_COMMIT is the commit, in the ftcdocs repository,
# from which we generated our po files.  We use it here so when we
# test build, we're building with the .rst files that generated our
# .po files.

FTCDOCS_CURRENT_COMMIT := {{translation.head}}
LANGUAGE := {{translation.language}}
BRANCH := {{translation.branch}}

EXCLUDED :=

# Internal variables

UPSTREAM := https://github.com/FIRST-Tech-Challenge/ftcdocs/

PYTHON := $(shell which python3)
MODE := html
JOBS := auto
ADDITIONAL_ARGS := --keep-going --color
SPHINXERRORHANDLING = -W

# Detect OS

ifeq '$(findstring ;,$(PATH))' ';'
    detected_OS := Windows
else
    detected_OS := $(shell uname 2>/dev/null || echo Unknown)
    detected_OS := $(patsubst CYGWIN%,Cygwin,$(detected_OS))
    detected_OS := $(patsubst MSYS%,MSYS,$(detected_OS))
    detected_OS := $(patsubst MINGW%,MSYS,$(detected_OS))
endif

ifeq ($(detected_OS),Darwin)        # Mac OS X
    CP_CMD := gcp                   # accessible with `brew install coreutils` or `brew upgrade coreutils`
else
    CP_CMD := cp
endif

.PHONY: all
all: ensure_prerequisites
	git -C venv/ftcdocs checkout $(FTCDOCS_CURRENT_COMMIT) || (git -C venv/ftcdocs fetch && git -C venv/ftcdocs checkout $(FTCDOCS_CURRENT_COMMIT))
	mkdir -p locales/$(LANGUAGE)/LC_MESSAGES/
	$(CP_CMD) -u --parents *.po */*.po locales/$(LANGUAGE)/LC_MESSAGES/
	$(MAKE) -C venv/ftcdocs/docs/ \
	  JOBS='$(JOBS)'             \
	  SPHINXOPTS='-D locale_dirs=$(abspath locales) \
	  -D language=$(LANGUAGE)           \
	  -D gettext_compact=0              \
	  $(ADDITIONAL_ARGS)'               \
	  SPHINXERRORHANDLING=$(SPHINXERRORHANDLING) \
	  $(MODE)
	@echo "Build success, open file://$(abspath venv/ftcdocs/)/docs/build/html/index.html or run 'make htmlview' to see them."

venv/ftcdocs/.git/HEAD:
	git clone https://github.com/FIRST-Tech-Challenge/ftcdocs/ venv/ftcdocs

.PHONY: ensure_prerequisites
ensure_prerequisites: venv/ftcdocs/.git/HEAD
	@if ! sphinx-build --version >/dev/null 2>&1; then \
	    git -C venv/ftcdocs/ checkout $(BRANCH); \
	    echo "You're missing dependencies please install:  "; \
	    echo "python -m pip install -r venv/ftcdocs/docs/requirements.txt"; \
	    exit 1; \
	fi

.PHONY: htmlview
htmlview: MODE=htmlview
htmlview: all

.PHONY: todo
todo: ensure_prerequisites
	potodo --exclude venv .venv $(EXCLUDED)

.PHONY: wrap
wrap: ensure_prerequisites
	@echo "Re wrapping modified files"
	powrap -m

.PHONY: spell
spell: ensure_prerequisites $(DESTS)

.PHONY: line-length
line-length:
	@echo "Searching for long lines..."
	@awk '{if (length(gensub(/శ్రీనివాస్/, ".", "g", $$0)) > 80 && length(gensub(/[^ ]/, "", "g")) > 1) {print FILENAME ":" FNR, "line too long:", $$0; ERRORS+=1}} END {if (ERRORS>0) {exit 1}}' *.po */*.po

.PHONY: sphinx-lint
sphinx-lint:
	@echo "Checking all files using sphinx-lint..."
	@sphinx-lint --enable all --disable line-too-long *.po */*.po */*/*.po */*/*/*.po */*/*/*/*.po */*/*/*/*/*.po

.PHONY: fuzzy
fuzzy: ensure_prerequisites
	potodo -f --exclude venv .venv $(EXCLUDED)

.PHONY: verifs
verifs: spell line-length sphinx-lint

.PHONY: clean
clean:
	@echo "Cleaning *.mo"
	rm -rf locales/$(LANGUAGE)/LC_MESSAGES/
	find -name '*.mo' -delete
	@echo "Cleaning build directory"
	git -C venv/ftcdocs/docs/ clean -xdf
