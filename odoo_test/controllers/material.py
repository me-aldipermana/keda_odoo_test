from odoo import http
from odoo.http import request


class MaterialAPIController(http.Controller):

    @http.route('/api/materials', auth='public', type='http', methods=['GET'], csrf=False)
    def get_materials(self, **kwargs):
        materials = request.env['material'].sudo().search([])
        data = []
        for material in materials:
            data.append({
                'code': material.code,
                'name': material.name,
                'type': material.type,
                'buy_price': material.buy_price,
                'supplier': material.supplier_id.name
            })
        return {'status': 200, 'data': data}

    @http.route('/api/materials', auth='public', type='http', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        try:
            if float(kwargs.get('buy_price', 0)) < 100:
                return {'status': 400, 'error': 'Buy price must be at least 100.'}

            new_material = request.env['material'].sudo().create({
                'code': kwargs.get('code'),
                'name': kwargs.get('name'),
                'type': kwargs.get('type'),
                'buy_price': kwargs.get('buy_price'),
                'supplier_id': kwargs.get('supplier_id')
            })
            return {'status': 201, 'id': new_material.id}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/materials', auth='public', type='http', methods=['PUT'], csrf=False)
    def create_material(self, **kwargs):
        try:
            if float(kwargs.get('buy_price', 0)) < 100:
                return {'status': 400, 'error': 'Buy price must be at least 100.'}

            code = kwargs.get('code', False)
            if not code:
                return {'status': 400, 'error': 'Code is required.'}

            material = request.env['material'].sudo().search([('code', '=', code)])
            if not material:
                return {'status': 400, 'error': f'Material with code {code} not found.'}

            name = kwargs.get('name', False)
            if name:
                material.name = name

            type = kwargs.get('type', False)
            if type:
                material.type = type

            buy_price = kwargs.get('buy_price', False)
            if buy_price:
                material.buy_price = buy_price

            supplier_id = kwargs.get('supplier_id', False)
            if supplier_id:
                material.supplier_id = supplier_id

            return {'status': 200, 'id': material.id}
        except Exception as e:
            return {'status': 500, 'error': str(e)}

    @http.route('/api/materials', auth='public', type='http', methods=['DELETE'], csrf=False)
    def create_material(self, **kwargs):
        try:
            code = kwargs.get('code', False)
            if not code:
                return {'status': 400, 'error': 'Code is required.'}

            material = request.env['material'].sudo().search([('code', '=', code)])
            if not material:
                return {'status': 400, 'error': f'Material with code {code} not found.'}
            
            material.unlink()

            return {'status': 200, 'id': material.id}
        except Exception as e:
            return {'status': 500, 'error': str(e)}