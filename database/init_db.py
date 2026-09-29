from database.connection import engine
from database.base import Base

def criar_banco():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    criar_banco()