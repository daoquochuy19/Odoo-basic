import datetime

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True, default="abc")
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', compute="calculate_age", inverse="calculate_dob", store=True)
    weight = fields.Float('Weight (kg)', default=1.00)
    dob = fields.Date('DOB')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                   relation='pet_product_rel',
                                   column1='col_pet_id',
                                   column2='col_product_id')
    basic_price = fields.Float('Basic Price', default=0)

    @api.model
    def create(self, vals):
        is_check_duplicated_pet_name = self.env['ir.config_parameter'].sudo().get_param(
            'mypet.is_check_duplicated_pet_name', default=False)
        if is_check_duplicated_pet_name:
            vals = [vals, ] if not isinstance(vals, (tuple, list)) else vals
            for val in vals:
                pet_name = val["name"]
                pet_records = self.search([('name', '=', pet_name)])
                if pet_records:
                    raise ValidationError(_("Duplicated pet name @ %s" % pet_name))
        return super(MyPet, self).create(vals)

    @api.depends('dob')
    def calculate_age(self):
        today = datetime.date.today()
        for rec in self:
            if rec.dob:
                dob = fields.Datetime.to_datetime(rec.dob).date()
                age_current = str(int((today - dob).days / 365))
                rec.age = age_current
            else:
                rec.age = "0"

    @api.depends('age')
    def calculate_dob(self):
        current_year = datetime.date.today().year
        for rec in self:
            if rec.age:
                year_dob = current_year - rec.age
                rec.dob = datetime.date.today().replace(year=year_dob)

    def custom_remove(self):
        for pet in self:
            pet.unlink()
        pass

    def write(self, vals):
        print("Write method is triggered", vals)
        return super(MyPet, self).write(vals)
