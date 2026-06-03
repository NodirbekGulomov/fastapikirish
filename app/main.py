class SessionLocal:
    pass


class Note:
    pass


def create_note(session: SessionLocal):
    note = Note()

    session.add(note)

    session.commit()
