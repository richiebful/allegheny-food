default: 2011_payment_data.zip 2011_name_address_file.zip foia_state_county_codes.xls loan_program_lookup.xls
	unzip -f 2011_payment_data.zip
	unzip -f 2011_name_address_file.zip
	libreoffice --headless --convert-to csv foia_state_county_codes.xls
	libreoffice --headless --convert-to csv loan_program_lookup.xls
	rename 's/.TXT/.csv/' *.TXT

2011_payment_data.zip:
	wget https://www.fsa.usda.gov/Internet/FSA_File/2011_payment_data.zip

2011_name_address_file.zip:
	wget https://www.fsa.usda.gov/Internet/FSA_File/2011_name_address_file.zip

foia_state_county_codes.xls:
	wget https://www.fsa.usda.gov/Internet/FSA_File/foia_state_county_codes.xls

loan_program_lookup.xls:
	wget https://www.fsa.usda.gov/Internet/FSA_File/loan_program_lookup.xls

clean:
	rm -f *.zip *.xls
