from async_fun import run_main
from models_db import Base

if __name__ == "__main__":
    run_main()
    Base.metadata.create_all()
