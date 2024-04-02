from odoo import  fields, models , api 
from odoo.exceptions import ValidationError
#from odoo import sql



class Building(models.Model):
    _name= 'building'
    _discription = 'Building Record'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    
    no = fields.Integer()
    code = fields.Char()
    discription = fields.Text()
    name = fields.Char()
    active = fields.Boolean(default =True)
    