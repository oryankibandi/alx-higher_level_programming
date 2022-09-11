#!/usr/bin/python3
"""
lists all State objects
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from swlalchemy import create_emgine

    Base.metadata.create_all(engine)

    engine = create_engine('mysql://{}:{}@localhost:5432/{}'
            .format(sys.argv[0], sys.argv[1], sys.argv[2]))

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format((state.id, state.name))

    session.close()
