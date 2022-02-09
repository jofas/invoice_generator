python3 invoice_generator.py examples/example1.json
cp build/invoice_nr_1.pdf examples/example1.pdf

jsonnet examples/example2.jsonnet | python3 invoice_generator.py -
cp build/invoice_nr_2.pdf examples/example2.pdf
