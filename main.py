from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Birthday(Field):
    def __init__(self, birthday=None):
        if birthday:
            self.value = birthday
        else:
            self.value = None


class Name(Field):
    def __init__(self, name):
        if name:
            self.value = name
        else:
            raise ValueError


class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.value = phone
        else:
            raise ValueError


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name).value
        self.phones = []
        self.birthday = Birthday(birthday).value

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone_for_remove):
        phone = self.find_phone(phone_for_remove)
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
        else:
            raise ValueError

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now()
            next_birthday = self.birthday.replace(year=today.year)
            if today > next_birthday:
                next_birthday = self.birthday.replace(year=today.year + 1)
            days_left = (next_birthday - today).days
            return days_left
        else:
            return None

    def find_phone(self, phone_number):
        for i in self.phones:
            if i.value == phone_number:
                return i

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, user):
        self.data.update({user.name: user})

    def find(self, name):
        return self.data[name] if name in self.data else None

    def delete(self, name):
        return self.data.pop(name) if name in self.data else None

    def iterator(self, n=10):
        records = list(self.data.values())
        for i in range(0, len(records), n):
            yield records[i:i + n]
