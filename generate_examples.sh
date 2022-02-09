python3 invoice_generator.py invoice examples/invoice_1.json
cp build/invoice_nr_1.pdf examples/invoice_1.pdf

jsonnet examples/invoice_2.jsonnet | python3 invoice_generator.py invoice -
cp build/invoice_nr_2.pdf examples/invoice_2.pdf
