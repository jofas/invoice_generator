class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return "{:02d}.{:02d}.{:04d}".format(self.day, self.month, self.year)

    @staticmethod
    def fromNamespace(n):
        if n is not None:
            return Date(
                day=n.day,
                month=n.month,
                year=n.year,
            )
        else:
            return None


class Address:
    def __init__(self, street, house_number, postal_code, place, country):
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.place = place
        self.country = country

    @staticmethod
    def fromNamespace(n):
        return Address(
            street=n.street,
            house_number=n.house_number,
            postal_code=n.postal_code,
            place=n.place,
            country=n.country,
        )


class Person:
    def __init__(self, address, company, name, phone, email):
        self.address = address
        self.company = company
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def fromNamespace(n):
        return Person(
            address=Address.fromNamespace(n.address),
            company=n.company,
            name=n.name,
            phone=n.phone,
            email=n.email,
        )


class PaymentDetails:
    def __init__(self, bank, iban, bic):
        self.bank = bank
        self.iban = iban
        self.bic = bic

    @staticmethod
    def fromNamespace(n):
        return PaymentDetails(
            bank=n.bank,
            iban=n.iban,
            bic=n.bic,
        )


class Entry:
    def __init__(self, description, price, start, end):
        self.start = start
        self.end = end
        self.description = description
        self.price = price

    @staticmethod
    def fromNamespace(n):
        return Entry(
            description=n.description,
            price=n.price,
            start=Date.fromNamespace(n.start),
            end=Date.fromNamespace(n.end),
        )


class Invoice:
    def __init__(
            self,
            sender,
            tax_id,
            payment_details,
            invoice_date,
            invoice_nr,
            recipient,
            entries):
        self.sender = sender
        self.tax_id = tax_id
        self.payment_details = payment_details
        self.invoice_date = invoice_date
        self.invoice_nr = invoice_nr
        self.recipient = recipient
        self.entries = entries

    @staticmethod
    def fromNamespace(n):
        return Invoice(
            sender=Person.fromNamespace(n.sender),
            tax_id=n.tax_id,
            payment_details=PaymentDetails.fromNamespace(n.payment_details),
            invoice_date=Date.fromNamespace(n.invoice_date),
            invoice_nr=n.invoice_nr,
            recipient=Person.fromNamespace(n.recipient),
            entries=[Entry.fromNamespace(i) for i in n.entries],
        )


class Letter:
    def __init__(
            self,
            sender,
            letter_date,
            letter_nr,
            recipient,
            headline,
            content,
            closing):
        self.sender = sender
        self.letter_date = letter_date
        self.letter_nr = letter_nr
        self.recipient = recipient
        self.headline = headline
        self.content = content
        self.closing = closing

    @staticmethod
    def fromNamespace(n):
        return Letter(
            sender=Person.fromNamespace(n.sender),
            letter_date=Date.fromNamespace(n.letter_date),
            letter_nr=n.letter_nr,
            recipient=Person.fromNamespace(n.recipient),
            headline=n.headline,
            content=n.content,
            closing=n.closing,
        )
