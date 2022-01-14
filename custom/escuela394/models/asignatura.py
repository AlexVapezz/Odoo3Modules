from odoo import models, fields, api

class Asignatura(models.Model):
    _name = 'escuela.asignatura'
    codigoAsig = fields.Integer('Codigo Asignatura', required=True)
    nombre = fields.Char('Nombre Asignatura', required=True)
    descripcion = fields.Text('Descripcion asignatura')
    temas = fields.Integer('Temas')


    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res