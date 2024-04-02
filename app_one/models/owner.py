from odoo import  fields, models , api 

class Owner(models.Model):
    _name='owner'
    
    name = fields.Char(required=True)
    phone = fields.Char()
    address = fields.Char ()
    property_ids = fields.One2many('property','owner_id')