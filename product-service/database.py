from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2://systemdev:systemdev@localhost/product')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
   
    from models import Product,Product_Item,Category,UOM
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    