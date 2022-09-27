from odoo import fields, models, api,_


class Prefix(models.Model):
    _name = "prefix"

    code=fields.Char(string="Prefix")
    name=fields.Char(related='code')
    code1=fields.Char(string="code", default=lambda self: self.env['ir.sequence'].next_by_code('prefix_increment'))

