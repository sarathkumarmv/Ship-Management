from openerp import models, fields
class Ship1(models.Model):

   _name = 'sales.ship'

   imo = fields.Char(string='IMO', required=True)
   _sql_constraints = [('IMO_unique', 'unique(imo)', 'imo number must be unique!')]
   _rec_name = 'imo'
   Hull_Number = fields.Integer(string='Hull_Number', required=True)
   Engine_Number = fields.Integer(string='Engine_Number', required=True)
   Vessel_Name = fields.Char(string='Vessel_Name ', required=True)
   Build_Year = fields.Integer(string='Build_Year', required=True)

   Ship_Yard = fields.Many2one('res.partner', string='Ship_Yard', required=True)
   Ship_Owner = fields.Many2one('res.partner', string='Ship_Owner', required=True)
   Ship_Management = fields.Many2one('res.partner', string='Ship_Management', required=True)
   Engine_Builder = fields.Many2one('res.partner', string='Engine_Builder', required=True)

class inherit_ship_order(models.Model):
   _inherit = 'sale.order'
   def writes(self, cr, uid, ids, context=None):
      sale_order_obj = self.browse(cr, uid, ids[0], context=context)
      sale_order_line_obj = self.pool.get('sale.order.line')

      for order in sale_order_obj:
         for line in order.order_line:
            sale_order_line_obj.write(cr, uid,line.id, {'shipping_line':order.shipping.id},context=context)

   shipping = fields.Many2one('sales.ship', 'Shipment ID', required=False, onupdate="cascade", ondelete="cascade")

class shipping_order_line(models.Model):
    _inherit = 'sale.order.line'
    shipping_line = fields.Many2one('sales.ship', 'Shipment ID', required=False, onupdate="cascade", ondelete="cascade")
