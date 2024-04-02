from odoo import  fields, models , api 
from odoo.exceptions import ValidationError
#from odoo import sql



class propert(models.Model):
    _name= 'property'
    _discription = 'Property'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    
    name= fields.Char(required=True, default= 'New')
    discription= fields.Text(tracking=1)
    postcode= fields.Char()
    data_available= fields.Date(tracking=1)
    expected_price= fields.Float()
    selling_price= fields.Float()
    dif = fields.Float(compute='_compute_diff')
    garden= fields.Boolean()
    expected_selling_date=fields.Date()
    is_late=fields.Boolean()
    garden_orientation= fields.Selection(
        [
            ('north', 'North'),
             ('south', 'South'),
            ],
        default='north')
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_Address = fields.Char(related = 'owner_id.address' )
    owner_phone = fields.Char(related = 'owner_id.phone')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','Closed'),
        ])
    
    
    _sql_constraints = [
                ('unique_name','unique(name)','name already exist')
             ]
    
    
    line_ids=fields.One2many('property.line','property_id')
    active = fields.Boolean(default =True)

    @api.constrains('selling_price')
    def _check_price(self):
        for rec in self:
            if rec.selling_price == 0.00:
                print ("not valid value")
                raise ValidationError('Please add valid price')
            
    @api.depends('expected_price','selling_price')        
    def _compute_diff(self):
        for rec in self:
            print("inside dependents")
            rec.dif = rec.expected_price - rec.selling_price
    
    
    @api.onchange('expected_price', 'owner_ide.phone')
    def _onchange_expected_price(self):
        for rec in self:
            print('on_change method')
        
    
    def action_draft(self):
        for rec in self:
            print('draft action')
            rec.state = 'draft'
            
    def action_pending(self):
        for rec in self:
            print ('pending ')
            rec.state = "pending"
       
    def action_closed(self):
        for rec in self: 
            rec.state = 'closed'
            
    def action_btn(self):
        print (self.env['property'].search([('name','!=','Daih')]))
       
       
    def action_owner(self):
       action = self.env['ir.actions.actions']._for_xml_id('app_one.owner_action')
       view_id = self.env.ref('app_one.owner_form').id
       action['res_id']= self.owner_id.id
       action['views']= [[view_id, 'form']]
       return action
        
        
    def check_expected_selling_Date(self):
        property_ids =self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True
                print(rec)     
                
class propertyLine(models.Model):
    _name= 'property.line'
    
    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char() 
                    