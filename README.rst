Invoice Generator
=================

Generates invoice PDFs from structured data using a LaTeX template.
The data is provided by a ``json/jsonnet`` file.


Example
-------

The example invoices in the ``examples/`` dir are generated via:

.. code:: bash

   python3 invoice_generator.py examples/example1.json && cp build/invoice_nr_1.pdf examples/example1.pdf
   jsonnet examples/example2.jsonnet | python3 invoice_generator.py - && cp build/invoice_nr_2.pdf examples/example2.pdf

**Note:** the number in the filename of the generated PDF comes from
the ``invoice_nr`` provided by the ``json`` input.


Dependencies
-------------

* ``tex-live (linux/macOs)`` or ``MikeTeX (Windows)`` with
  ``lualatex`` installed

* ``python 3``

* the ``jinja2`` and ``fire`` python packages
