from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class EagleeduApplication(models.Model):
    _name = 'eagleedu.application'

    #_inherit = 'res.partner'
    #_inherit = ['mail.thread']
    # _description = 'Applications for the admission'
    # _order = 'id desc'


    application_date = fields.Datetime('application Date', default=lambda
        self: fields.datetime.now())  # , default=fields.Datetime.now, required=True

    stu_name = fields.Char(string='Student Name', required=True, help="Enter Name of Student")
    stu_name_b = fields.Char(string='Student Bangla Name')
    stu_image = fields.Binary(string='Image', help="Provide the image of the Student")
    stu_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=True)
    stu_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    stu_mother_name = fields.Char(string="mother's Name", help="Proud to say my mother is",required=True)
    stu_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="mother's Mobile No", help="mother's Mobile No")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=True, track_visibility='onchange',
                                help="Your Gender is ")
    date_of_birth = fields.Date(string="Date Of birth", required=True, help="Enter your DOB")

    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                help="Select the Nationality")

    street = fields.Char(string='Street', help="Enter the street")
    street2 = fields.Char(string='Street2', help="Enter the street2")
    zip = fields.Char(change_default=True, string='ZIP code', help="Enter the Zip Code")
    city = fields.Char(string='City', help="Enter the City name")
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               help="Select the State where you are from")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19,
                                 help="Select the Country")
    is_same_address = fields.Boolean(string="Permanent Address same as above", default=True,
                                     help="Tick the field if the Present and permanent address is same")
    per_street = fields.Char(string='Street', help="Enter the street")
    per_street2 = fields.Char(string='Street2', help="Enter the street2")
    per_zip = fields.Char(change_default=True, string='ZIP code', help="Enter the Zip Code")
    per_city = fields.Char(string='City', help="Enter the City name")
    per_state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                                   help="Select the State where you are from")
    per_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19,
                                     help="Select the Country")
    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is")

    religious_id = fields.Many2one('eagleedu.religious', string="Religious", help="My Religion is ")



    eagleedu_application_no = fields.Char(string='Application No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))




    @api.model
    def create(self, vals):
    #     """Overriding the create method and assigning the the sequence for the record"""
         if vals.get('eagleedu.application', _('New')) == _('New'):
            vals['eagleedu_application_no'] = self.env['ir.sequence'].next_by_code('seq.eagleedu.application') or _('New')
         res = super(EagleeduApplication, self).create(vals)
         return res

class EagleeduReligious(models.Model):
        _name = 'eagleedu.religious'
        name = fields.Char()