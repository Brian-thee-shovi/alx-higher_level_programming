#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    my_state = State(name="Louisiana")
    session.add(my_state)
    session.commit()
    s = session.query(State).filter_by(name="Louisiana").first()

    if s:
        print(s.id)

    session.close()