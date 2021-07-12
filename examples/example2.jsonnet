local types = import '../types.libsonnet';

types.Invoice(
  sender=types.Person(
    address=types.Address(
      street='Hauptstraße',
      house_number='69',
      postal_code='45257',
      place='Essen',
    ),
    company='Thyssen Krupp',
    phone='02218/224466',
    email='xyz@abc.de',
  ),
  tax_id='LMN/OPQ/RSTU',
  iban='DE5454545454545454545454',
  invoice_date=types.Date(6, 7, 2021),
  invoice_nr=2,
  recipient=types.Person(
    address=types.Address(
      street='Am Hinseldaunenweg',
      house_number='18',
      postal_code='50667',
      place='Köln',
    ),
    company='Siemens AG',
  ),
  entries=[
    types.Entry(
      description='Irgendeine Dienstleistung',
      price=25000.0,
      start=types.Date(3, 3, 2021),
      end=types.Date(6, 7, 2021),
    ),
    types.Entry(
      description='Irgendeine andere Dienstleistung',
      price=20170.0,
      start=types.Date(5, 5, 2021),
      end=types.Date(6, 6, 2021),
    ),
    types.Entry(
      description='Irgendeine coole Machine',
      price=80000.0,
      start=types.Date(6, 7, 2021),
    ),
  ],
)
