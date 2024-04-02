from odoo import  fields, models , api 

class Tag(models.Model):
    _name='tag'
    
    
    name= fields.Char(required=True)