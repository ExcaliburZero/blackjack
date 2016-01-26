PACKAGE = blackjack

help:
	@echo "  test           runs tests"
	@echo "  testcoverage   runs tests with coverage"
	@echo "  pylint         runs pylint on the package"

test:
	nosetests --cover-package=$(PACKAGE)

testcoverage:
	nosetests --with-coverage --cover-package=$(PACKAGE)

pylint:
	pylint $(PACKAGE) --rcfile=pylint.conf
