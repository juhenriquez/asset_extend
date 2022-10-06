from odoo import fields, models, api,_


class AssetAccount(models.Model):
    _inherit = "account.asset"

    code1=fields.Char(related="prefix.code",store=True)
    code_2=fields.Char(related="prefix.code1",store=True)
    r_dep=fields.Many2one("departamento",string='Departamento responsable')
    a_ub=fields.Many2one("ubicacion",string="Area de ubicación")
    comment1=fields.Char(string='Comentario')
    f_asset=fields.Char(string="Familia de activos")
    gen_codigo=fields.Char(string="Generacion codigo", default=lambda self: _('New'))
    label1=fields.Char(string='Creacion de etiquetas')
    prefix=fields.Many2one("prefix",string="prefix")
    sequence_id = fields.Many2one(
        'ir.sequence', 'Reference Sequence',
        check_company=True, copy=False)
    code2=fields.Char()
    code3=fields.Char()
    
    @api.onchange("prefix")
    def get_prefix(self):
        self.code2=self.code1
        self.code3=self.code_2

    @api.model
    def create(self, vals):

        
        if 'sequence_id' not in vals or not vals['sequence_id']:
            
            
            vals['sequence_id'] = self.env['ir.sequence'].sudo().create({
                'name': vals['name'],
                'prefix': vals['code2'],
                'company_id': self.company_id.id,
                'padding': 5,
                'code':vals['code3'],
            }).id
        if vals.get('gen_codigo', _('New')) == _('New'):
            vals['gen_codigo'] = self.env['ir.sequence'].next_by_code(vals['code3']) or _('New')
        res=super(AssetAccount, self).create(vals)
        return res

class Ubicacion(models.Model):
    _name = "ubicacion"

    name=fields.Char("Nombre")

class Departamentp(models.Model):
    _name = "departamento"

    name=fields.Char("Nombre")
 