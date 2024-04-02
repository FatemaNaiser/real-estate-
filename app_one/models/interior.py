from odoo import  fields, models , api 

class interior(models.Model):
    _name='interior'
    
    interior_name = fields.Char()
    Client_name = fields.Char()
    Area= fields.Float() 
    floor = fields.Integer()  
    price = fields.Float()

def action_calc(self):
    for rec in self: 
        if rec.floor == 1 : 
            #rec.price = "1200 BD"
            print ("calculate function")