# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
	_inherit = 'account.config.settings'

	dir_json = fields.Char('Working Directory')

	@api.multi
	def get_dir_json(self):
		ir_values = self.env['ir.values']
		dir_json = ir_values.get_default('account.config.settings', 'dir_json')
		return dir_json

	
	@api.multi
	def set_dir_json(self):
		return self.env['ir.values'].sudo().set_default(
			'account.config.settings', 'dir_json', self.dir_json)