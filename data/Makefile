SUPPLEMENTARY_CSV=foia_state_county_codes.csv loan_program_lookup.xls
SUPPLEMENTARY_XLS=$(SUPPLEMENTARY_CSV:.csv=.xls)
PAYMENT_ZIP=2008_payment_data.zip 2009_payment_data.zip 2010_payment_data.zip 2011_payment_data.zip
PAYMENT_TXT=CAS.WDC11019.PMT08.FINAL.DT11186.csv CAS.WDC11019.PMT09.FINAL.DT11186.csv CAS.WDC11019.PMT10.FINAL.DT11186.csv CAS.WDC11019.PMT11.FINAL.DT11186.csv
NAME_ADDR_ZIP=2008_name_address_file.zip 2009_name_address_file.zip 2010_name_address_file.zip 2011_name_address_file.zip
NAME_ADDR_TXT=CAS.WDC11019.NA08.FINAL.DT11186.csv CAS.WDC11019.NA09.FINAL.DT11186.csv CAS.WDC11019.NA10.FINAL.DT11186.csv CAS.WDC11019.NA11.FINAL.DT11186.csv

all: $(SUPPLEMENTARY_CSV) $(PAYMENT_TXT) $(NAME_ADDR_TXT)
	#standardizes 2009-11 NA/Payment filenames
	rename 's/.TXT/.csv/' *.TXT
	#standardizing 2008 NA/Payment filenames
	rename 's/$XTR/CAS.WDC11019/' XTR.*08.FINAL.DT10189.txt
	rename '\.DT10189\.txt/\.DT11186\.csv/' CAS.WDC11019.*08.FINAL.DT10189.txt

fedora: $(SUPPLEMENTARY_CSV) $(PAYMENT_TXT) $(NAME_ADDR_TXT)
	#standardizes 2009-11 NA/Payment filenames
	rename '.TXT' '.csv' *.TXT
	#standardizing 2008 NA/Payment filenames
	rename 'XTR' 'CAS.WDC11019' XTR.*08.FINAL.DT10189.txt
	rename '.DT10189.txt' '.DT11186.csv' CAS.WDC11019.*08.FINAL.DT10189.txt

clean:
	rm -f *.csv *.xls

$(SUPPLEMENTARY_CSV): $(SUPPLEMENTARY_XLS)
	libreoffice --headless --convert-to csv foia_state_county_codes.xls
	libreoffice --headless --convert-to csv loan_program_lookup.xls

$(NAME_ADDR_ZIP): $(NAME_ADDR_ZIP)
	unzip -u 2008_name_address_file.zip
	unzip -u 2009_name_address_file.zip
	unzip -u 2010_name_address_file.zip
	unzip -u 2011_name_address_file.zip

$(PAYMENT_TXT): $(PAYMENT_ZIP)
	unzip -u 2008_payment_data.zip
	unzip -u 2009_payment_data.zip
	unzip -u 2010_payment_data.zip
	unzip -u 2011_payment_data.zip

$(SUPPLEMENTARY_XLS):
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/loan_program_lookup.xls
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/foia_state_county_codes.xls

$(NAME_ADDR_ZIP):
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2008_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2009_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2010_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2011_name_address_file.zip

$(PAYMENT_ZIP):
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2008_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2009_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2010_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2011_payment_data.zip
