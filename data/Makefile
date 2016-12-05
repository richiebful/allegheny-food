default: supplementaryPaymentCSV paymentTextFiles
	#standardizes 2009-11 NA/Payment filenames
	rename 's/.TXT/.csv/' *.TXT
	#standardizing 2008 NA/Payment filenames
	rename 's/$XTR/CAS.WDC11019/' XTR.*08.FINAL.DT10189.txt
	rename 's/\.DT10189\.txt/\.DT11186\.csv/' CAS.WDC11019.*08.FINAL.DT10189.txt

clean:
	rm -f *.csv *.xls

supplementaryPaymentCSV:
	libreoffice --headless --convert-to csv foia_state_county_codes.xls
	libreoffice --headless --convert-to csv loan_program_lookup.xls	

paymentTextFiles: paymentDownload
	unzip -u 2008_payment_data.zip
	unzip -u 2008_name_address_file.zip
	unzip -u 2009_payment_data.zip
	unzip -u 2009_name_address_file.zip
	unzip -u 2010_payment_data.zip
	unzip -u 2010_name_address_file.zip
	unzip -u 2011_payment_data.zip
	unzip -u 2011_name_address_file.zip
	

supplementaryPaymentExcel:
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/loan_program_lookup.xls
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/foia_state_county_codes.xls

paymentDownload:
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2008_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2008_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2009_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2009_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2010_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2010_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2011_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2011_payment_data.zip
	
