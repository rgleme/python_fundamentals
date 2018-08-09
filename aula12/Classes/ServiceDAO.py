#!/usr/bin/python

from Classes.Service import Service as ServiceClass
from Classes.Client import Client as ClientClass
from Classes.Product import Product as ProductClass
from Models.Models import Service as ServiceTable,Client,Product, session

class ServiceDAO:

    def __init__(self,service=""):
        self.service = service
    def get(self):
        try:
            service = session.query(ServiceTable,Client,Product).join(Client,Product).filter(ServiceTable.id==1).first()
			
            if service is None:
                return None
            else:
                c = ClientClass(service.Client.name,service.Client.cpf,service.Client.segment)
                c.id = service.Client.id

                p = ProductClass(service.Product.name,service.Product.description,service.Product.image)
                p.id = service.Product.id

                s = ServiceClass(service.Service.request_date,service.Service.cancel_date)
                s.id = service.Service.id
                s.client = c
                s.product = p
                return s

        except Exception as e:
            print "Deu erro: "%e
