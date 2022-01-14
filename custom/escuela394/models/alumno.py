from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'escuela.alumno'
    codigoAlu = fields.Integer('Codigo alumno', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    fecha = fields.Date(string='Fecha De Nacimiento', default=lambda s: fields.Date.context_today(s))
    cp = fields.Integer('Codigo Postal', required=True)
    direccion = fields.Char('Direccion', required=True)
    codigoProf = fields.Many2one('escuela.profesor', 'Codigo Profesor')
    asignatura = fields.Many2many('escuela.asignatura', string='asignatura')

    def name_get(self):
        res = []
        for record in self:
            tipo = record.nombre
            res.append((record.id, tipo))
        return res