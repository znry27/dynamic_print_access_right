# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval


class PrintAccessRight(models.Model):
    _name = "print.access.right"
    _description = "Print Access Right"
    _order = "priority asc"

    name = fields.Char()
    document_id = fields.Many2one('ir.actions.report')
    priority = fields.Integer(default=10)
    error_message = fields.Text()
    active = fields.Boolean(default=True)
    type = fields.Selection([
        ('fixed', 'Fixed'),        
        ('fixed_limit_count', 'Fixed Print Count'),
        ('by_condition', 'By Condition'),
        ('by_condition_limit_count', 'By Condition and Print Count')
    ], default='fixed')
    max_print_count = fields.Integer(default=0)
    apply_to_all_user = fields.Boolean(default=True)
    apply_to_user_ids = fields.Many2many('res.users', string='Apply to Specific User')
    condition = fields.Char()
    condition_model = fields.Char(default='product.product')


    @api.onchange('document_id')
    def onchange_document_id(self):
        if self.document_id:
            self.condition_model = self.document_id.model
            self.condition = '[]' if not self.condition else False

    def set_active(self):
        for rec in self:
            rec.active = True

    def set_inactive(self):
        for rec in self:
            rec.active = False

    def is_condition_match(self, active_id):
        if self.condition:
            domain = safe_eval(self.condition) + [('id', '=', active_id)]
            return bool(self.env[self.document_id.model].search_count(domain))
        else:
            return False

    def is_can_print(self, action_id, user_id, active_ids):
        acc_rights = self.sudo().search([('document_id','=',action_id)])
        
        for acc_right in acc_rights:
            if acc_right.type == 'fixed':
                print('A=')
                if acc_right.apply_to_all_user or (not acc_right.apply_to_all_user and user_id in acc_right.apply_to_user_ids.ids):
                    raise ValidationError(acc_right.error_message)

            elif acc_right.type == 'fixed_limit_count':
                print('B')
                for active_id in active_ids:
                    print_count = self.env['print.count'].sudo().search([('document_id','=',action_id), ('user_id','=',user_id), ('active_id','=',active_id)],limit=1)
                    if not print_count:
                        print_count = self.env['print.count'].sudo().create({
                            'document_id': action_id,
                            'user_id': user_id,
                            'count': 0,
                            'active_id': active_id
                        })
                    if (print_count.count + 1 ) > acc_right.max_print_count and (acc_right.apply_to_all_user or (not acc_right.apply_to_all_user and user_id in acc_right.apply_to_user_ids.ids)):
                        raise ValidationError(acc_right.error_message)
                    else:
                        print_count.count = print_count.count + 1

            elif acc_right.type == 'by_condition':
                print('C=')
                for active_id in active_ids:
                    if acc_right.is_condition_match(active_id):
                        if (acc_right.apply_to_all_user or (not acc_right.apply_to_all_user and user_id in acc_right.apply_to_user_ids.ids)):
                            raise ValidationError(acc_right.error_message)

            elif acc_right.type == 'by_condition_limit_count':
                print('D=')
                for active_id in active_ids:
                    if acc_right.is_condition_match(active_id):
                        print_count = self.env['print.count'].sudo().search([('document_id','=',action_id), ('user_id','=',user_id), ('active_id','=',active_id)],limit=1)
                        if not print_count:
                            print_count = self.env['print.count'].sudo().create({
                                'document_id': action_id,
                                'user_id': user_id,
                                'count': 0,
                                'active_id': active_id
                            })
                        if (print_count.count + 1 ) > acc_right.max_print_count and (acc_right.apply_to_all_user or (not acc_right.apply_to_all_user and user_id in acc_right.apply_to_user_ids.ids)):
                            raise ValidationError(acc_right.error_message)
                        else:
                            print_count.count = print_count.count + 1

class ActionReport(models.Model):
    _inherit = "ir.actions.report"

    print_count_ids = fields.One2many('print.count','document_id')

    def _render_qweb_pdf(self, res_ids=None, data=None):
        self.env['print.access.right'].sudo().is_can_print(self.id, self.env.user.id, res_ids)

        return super(ActionReport, self)._render_qweb_pdf(res_ids=res_ids, data=data)


class PrintCount(models.Model):
    _name = "print.count"
    _description = "Print Count"

    document_id = fields.Many2one('ir.actions.report')
    user_id = fields.Many2one('res.users')
    count = fields.Integer(default=0)
    active_id = fields.Integer(default=0)

    