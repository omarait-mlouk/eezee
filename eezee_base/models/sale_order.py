from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError


def _get_last_year_date():
    return datetime.now() - timedelta(days=365)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    old_delivery_status = fields.Selection(
        [
            ('normal', 'Normal'),
            ('late', 'Late')
        ],
        compute="_on_compute_commitment_date",
        store=True,
        default='normal'
    )
    sale_approved = fields.Boolean(default=False)

    @api.depends('commitment_date')
    def _on_compute_commitment_date(self):
        last_year_date = _get_last_year_date()
        for record in self:
            if record.commitment_date and record.commitment_date < last_year_date:
                record.old_delivery_status = 'late'
            else:
                record.old_delivery_status = 'normal'

    def action_sale_approve(self):
        self.sale_approved = True

    def action_confirm(self):
        # Iterate through each sale order
        for order in self:
            # Check if there is a condition that needs to be met before confirming the sale order
            if not order.sale_approved:  # Replace condition_not_met with your actual condition
                # If the condition is not met, raise a user error
                raise UserError("Cannot confirm sale order it has to be approved by the sale approver.")
        # If all conditions are met, call the original action_confirm method to proceed with the confirmation process
        return super(SaleOrder, self).action_confirm()

    @api.model
    def create(self, vals):
        if not vals.get('sale_approved'):
            # Add code to create activity
            self.env['mail.activity'].create({
                'res_id': vals.get('user_id'),
                'res_model_id': self.env['ir.model'].search([('model', '=', 'sale.order')], limit=1).id,
                'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                'summary': 'Approve Sale Order',
            })
        return super(SaleOrder, self).create(vals)
