class SessionLocal:
    pass


class Note:
    pass


def create_note():
    note=Note()
    
    with SessionLocal()as session:
        session.add(note)
        
        session.commit()
