Invoice Generator
=================

Generates invoice PDFs from structured data using a LaTeX template.
The data is provided by a ``json/jsonnet`` file.
Also supports the generation of business letters.


Example
-------

The example documents in the ``examples/`` dir are generated via:

.. code:: bash

   sh generate_examples.sh

**Note:** the number in the filename of the generated PDF comes from
the ``invoice_nr``/``letter_nr`` provided by the ``json`` input.


Dependencies
-------------

* ``tex-live (linux/macOs)`` or ``MikeTeX (Windows)`` with
  ``lualatex`` installed

* ``python 3``

* the ``jinja2`` and ``fire`` python packages


TODO
----

* offer generator

* ``Date`` type to simple date string
