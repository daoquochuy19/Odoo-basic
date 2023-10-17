from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

# ke thua chinh sua field, model, luu chung database


class MyPetPlus(models.Model):
    _name = "my.pet"
    _inherit = "my.pet"
    _description = "Extend mypet model"

    # add new field
    toy = fields.Char('Pet Toy', required=False)
    abc = fields.Char('Test add node before gender', required=False)

    # modify old fields
    # age = fields.Integer('Pet Age', default=2)
    gender = fields.Selection(selection_add=[('sterilization', 'Sterilization')])

    # practice constrains

    @api.constrains('toy')
    def no_ball(self):
        for record in self:
            if record.toy == 'ball':
                raise ValidationError("don't play with ball")

