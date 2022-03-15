from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,String,Text,Column,ForeignKey
from sqlalchemy.orm import backref, relationship


Base = declarative_base()


class Category(Base):
    """Category table fields"""

    __tablename__ = "category"

    id = Column(Integer , primary_key = True, autoincrement = "auto")
    name = Column(String(255) , unique = True , nullable = False)
    description = Column(Text , nullable = False)

    def __repr__(self):
        return "<Category %r>" % self.name

class Product(Base):
    """Product table fields"""

    __tablename__ =  "product"

    id = Column(Integer,primary_key= True,autoincrement="auto")
    name = Column(String,unique=True,nullable=False)
    description = Column(String(255),nullable=False)
    category_id = Column(Integer,ForeignKey('category.id')) #relationship added


    """on deleting a category , a product is deleted as well"""

    category = relationship(Category, backref = backref('products', uselist=True, cascade='delete,all'))


    def __repr__(self):
        """Stringify model."""
        return str(self.name)


class UOM(Base):
    """ UOM table fields"""

    __tablename__ = "uom"

    id = Column(Integer, primary_key = True, autoincrement = "auto")
    name = Column(String(255), unique = True, nullable = False)

    def __repr__(self):
        return str(self.name)
       


class Product_Item(Base):
    """Product_item table fields"""

    __tablename__ = "product_item"

    id = Column(Integer,primary_key=True,autoincrement="auto")
    product_id = Column(Integer,ForeignKey ("product.id")) #relationship added 
    name = Column(String , unique = True , nullable = False)
    description = Column(Text , nullable = False)
    uom_id = Column(Integer ,ForeignKey ("uom.id")) #relationship added

    
    """on_deleting a product or a uom , a Product_Item is deleted"""
    product = relationship(Product, backref = backref('product_items', uselist=True, cascade='delete,all'))
    uom = relationship(UOM, backref = backref('product_items', uselist=True, cascade='delete,all'))


    def __repr__(self):
        return str(self.name)



