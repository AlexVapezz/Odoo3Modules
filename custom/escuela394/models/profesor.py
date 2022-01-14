from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'escuela.profesor'
    imagen = fields.Binary('foto')
    codigoProf = fields.Integer('Codigo Del profesor', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    fecha = fields.Date(string='Fecha De Nacimiento', default=lambda s: fields.Date.context_today(s))
    cp = fields.Integer('Codigo Postal', required=True)
    direccion = fields.Char('Direccion', required=True)


    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res