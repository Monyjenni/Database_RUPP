class Config:    
    def __init__(self):
        self.DEBUG = True
        self.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:012345678@localhost:3306/apdb'
