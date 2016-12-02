default: supplementaryPaymentRawData paymentRawData
	unzip -u 2008_payment_data.zip
	unzip -u 2008_name_address_file.zip
	unzip -u 2009_payment_data.zip
	unzip -u 2009_name_address_file.zip
	unzip -u 2010_payment_data.zip
	unzip -u 2010_name_address_file.zip
	unzip -u 2011_payment_data.zip
	unzip -u 2011_name_address_file.zip
	libreoffice --headless --convert-to csv foia_state_county_codes.xls
	libreoffice --headless --convert-to csv loan_program_lookup.xls
	rename 's/.TXT/.csv/' *.TXT

clean:
	rm -f *.csv *.xls

supplementaryPaymentRawData:
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/loan_program_lookup.xls
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/foia_state_county_codes.xls

paymentRawData:
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2008_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2008_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2009_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2009_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2010_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2010_payment_data.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2011_name_address_file.zip
	wget -N https://www.fsa.usda.gov/Internet/FSA_File/2011_payment_data.zip
	
