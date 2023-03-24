import csv
from datetime import datetime

from Note import Note

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class NotesApp:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    # Проверяем, что строка не пустая
                    if len(row) > 0:
                        note = Note(int(row[0]), row[1], row[2], datetime.strptime(row[3], DATE_FORMAT),
                                    datetime.strptime(row[4], DATE_FORMAT))
                        self.notes.append(note)
        except FileNotFoundError:
            print(f"{self.file_name} not found. Starting with empty notes list.")

    def save_notes(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.truncate()  # очистить файл перед записью
            writer = csv.writer(file, delimiter='|')
            for note in self.notes:
                writer.writerow(
                    [note.id, note.title, note.body, note.created_at.strftime(DATE_FORMAT),
                     note.updated_at.strftime(DATE_FORMAT)])

    def add_note(self, title, body):
        id = self.get_max_id() + 1
        note = Note(id, title, body)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        for note in self.notes:
            print(note)

    def find_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def edit_note_by_id(self, id, title, body):
        note = self.find_note_by_id(id)
        if note:
            note.update(title, body)
            self.save_notes()
            print(f"Note #{note.id} updated.")
        else:
            print(f"Note #{id} not found.")

    def delete_note_by_id(self, id):
        note = self.find_note_by_id(id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print(f"Note #{id} deleted.")
        else:
            print(f"Note #{id} not found.")

    def get_max_id(self):
        if not self.notes:
            return 0
        return max(note.id for note in self.notes)
