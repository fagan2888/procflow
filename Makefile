MONITORING_DIR=build/monitoring
OUTPUT_DIR=build
DATA_DIR=data
CODE=code

help:
	@echo 'Makefile for a data driven process build                               '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make data                  download or generate relevant input data '
	@echo '   make process               run set of processes                     '
	@echo '   make clean_build           clean the build directory                '
	@echo '   make clean_data            clean the data directory                 '

setup:
	mkdir -p $(OUTPUT_DIR) $(DATA_DIR) $(MONITORING_DIR)

example: setup exampledata
	python $(CODE)/example.py $(OUTPUT_DIR) -d $(DATA_DIR) -m $(MONITORING_DIR)

exampledata: setup
	python $(CODE)/exampledata.py $(DATA_DIR)

clean_data:
	rm -rf $(DATA_DIR)/*

clean_build:
	rm -rf $(OUTPUT_DIR)/*

.PHONY: clean_data clean_build setup example exampledata 
