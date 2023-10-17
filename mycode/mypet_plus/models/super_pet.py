from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


# ke thua copy field, phuong thuc trong model truoc, luu database bang khac

class SuperPet(models.Model):
    _name = "super.pet"  # <- new model name
    _inherit = "my.pet"  # <- inherit fields and methods from model "my.pet"
    _description = "Prototype inheritance"

    # add new field
    is_super_strength = fields.Boolean("Is Super Strength", default=False)
    is_fly = fields.Boolean("Is Fly", default=False)
    planet = fields.Char("Planet")

    # avoid error: TypeError: Many2many fields super.pet.product_ids and my.pet.product_ids use the same table and columns
    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                   relation='super_pet_product_rel',  # <- change this relation name!
                                   column1='col_pet_id',
                                   column2='col_product_id')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], default='draft', string='Status', required='True')

    # practice onchange
    @api.onchange('planet')
    def fly(self):
        for rec in self:
            if rec.planet == 'venus':
                rec.is_fly = True
            elif rec.planet == 'earth':
                rec.is_fly = False

    def custom_remove(self):
        for pet in self:
            pet.unlink()
        pass

    def button_cancel(self):
        self.write({'state': 'cancel'})

    def button_draft(self):
        self.write({'state': 'draft'})

    def button_done(self):
        self.write({'state': 'done'})

    def button_progress(self):
        self.write({'state': 'in_progress'})
