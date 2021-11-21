import sys
import pathlib
import subprocess
import locale
import json
from types import SimpleNamespace

from jinja2 import Environment, PackageLoader
import fire


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
    def __init__(self, address, company, email):
        self.address = address
        self.company = company
        self.email = email

    @staticmethod
    def fromNamespace(n):
        return Person(
            address=Address.fromNamespace(n.address),
            company=n.company,
            email=n.email,
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
            iban,
            invoice_date,
            invoice_nr,
            recipient,
            entries):
        self.sender = sender
        self.tax_id = tax_id
        self.iban = iban
        self.invoice_date = invoice_date
        self.invoice_nr = invoice_nr
        self.recipient = recipient
        self.entries = entries

    @staticmethod
    def fromNamespace(n):
        return Invoice(
            sender=Person.fromNamespace(n.sender),
            tax_id=n.tax_id,
            iban=n.iban,
            invoice_date=n.invoice_date,
            invoice_nr=n.invoice_nr,
            recipient=Person.fromNamespace(n.recipient),
            entries=[Entry.fromNamespace(i) for i in n.entries],
        )


def main(filename="-"):
    locale.setlocale(locale.LC_ALL, locale="de_DE.UTF-8")

    env = Environment(
        loader=PackageLoader(__name__),
    )

    template = env.get_template("invoice.tex")

    if filename == "-":
        stream = sys.stdin.read()
    else:
        with open(filename) as file:
            stream = file.read()

    invoice = Invoice.fromNamespace(json.loads(
        stream,
        object_hook=lambda d: SimpleNamespace(**d),
    ))

    sum_ = sum([entry.price for entry in invoice.entries])
    tax = sum_ * 0.19

    pathlib.Path("./build").mkdir(exist_ok=True)

    filename = "./build/invoice_nr_{}.tex".format(invoice.invoice_nr)

    with open(filename, "w") as file:
        file.write(template.render(
            sender=invoice.sender,
            tax_id=invoice.tax_id,
            iban=invoice.iban,
            invoice_nr=invoice.invoice_nr,
            invoice_date=invoice.invoice_date,
            recipient=invoice.recipient,
            entries=invoice.entries,
            tax=tax,
            sum_=sum_,
            locale=locale,
        ))

    # run two times to make sure everything is build correctly
    # (e.g. latex needs two compilations to get the table of contents
    # right)
    subprocess.run(
        ["lualatex", "--output-directory=./build", filename])
    subprocess.run(
        ["lualatex", "--output-directory=./build", filename])


if __name__ == "__main__":
    fire.Fire(main)
