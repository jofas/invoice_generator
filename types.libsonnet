{
  Date(day, month, year): {
    day: day,
    month: month,
    year: year,
  },
  Address(street, house_number, postal_code, place, country='Deutschland'): {
    street: street,
    house_number: house_number,
    postal_code: postal_code,
    place: place,
    country: country,
  },
  Person(address, company, phone=null, email=null): {
    address: address,
    company: company,
    phone: phone,
    email: email,
  },
  PaymentDetails(bank, iban, bic): {
    bank: bank,
    iban: iban,
    bic: bic,
  },
  Entry(description, price, start, end=null): {
    description: description,
    price: price,
    start: start,
    end: end,
  },
  Invoice(sender, tax_id, payment_details, invoice_date, invoice_nr, recipient, entries): {
    sender: sender,
    tax_id: tax_id,
    payment_details: payment_details,
    invoice_date: invoice_date,
    invoice_nr: invoice_nr,
    recipient: recipient,
    entries: entries,
  },
}
