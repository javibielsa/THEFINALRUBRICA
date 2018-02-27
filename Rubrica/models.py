# -*- coding: utf-8 -*-

from odoo import models, fields

    
class carDealership(models.Model):
    _name = 'thefinalrubrica.carDealership'

    direction = fields.Char(String="Name", required=True)
    workers_ids = fields.One2many('thefinalrubrica.workers', 'carDealership_id', string="Workers")
    tools_ids = fields.One2many('thefinalrubrica.tools', 'carDealership_id', string="Tools")
    vehicles_ids = fields.One2many('thefinalrubrica.vehicles', 'carDealership_id', string="Vehicles")
    customers_ids = fields.One2many('thefinalrubrica.customers', 'carDealership_id', string="Customers")


class workers(models.Model):
	_name = 'thefinalrubrica.workers'
    
    name = fields.Char()
    date_of_birth = fields.Date()
    age = fields.Integer()customers
    carDealership_id = fields.Many2one('thefinalrubrica.carDealership', string="CarDealership", ondelete = 'cascade')
    tools_ids = fields.Many2many(string= "ToolsUse" , comodel_name = 'thefinalrubrica.tools', relation = 'rel_workers_tools', column1='workers', column2='tools')
    vehicles_ids = fields.Many2many(string= "Something" , comodel_name = 'thefinalrubrica.vehicles', relation = 'rel_workers_vehicles', column1='workers', column2='vehicles')


class tools(models.Model):
	_name = 'thefinalrubrica.tools'

	name = fields.Char(String="Name", required=True)
	tool_type = fields.Char()
	carDealership_id = fields.Many2one('thefinalrubrica.carDealership', string="CarDealership", ondelete = 'cascade')
	workers_ids = fields.Many2many(string= "WorkerTools" , comodel_name = 'thefinalrubrica.workers', relation = 'rel_workers_tools', column1='tools', column2='workers')


class vehicles(models.Model):
	_name = 'thefinalrubrica.vehicles'

	matricula = fields.Char(String="NumberPlate", required=True)
	name = fields.Char()
	color = fields.Char()
	carDealership_id = fields.Many2one('thefinalrubrica.carDealership', string="CarDealership", ondelete = 'cascade')
	workers_ids = fields.Many2many(string= "Something" , comodel_name = 'thefinalrubrica.workers', relation = 'rel_workers_vehicles', column1='vehicles', column2='workers')
	customers_id = fields.Many2one('thefinalrubrica.customers', string="Customers", ondelete = 'cascade')


class customers(models.Model):
	_name = 'thefinalrubrica.customers'

	name = fields.Char(String="Name", required=True)
    age = fields.Integer()
    country = fields.Char(String="Country", required=True)
    carDealership_id = fields.Many2one('thefinalrubrica.carDealership', string="CarDealership", ondelete = 'cascade')
    vehicles_ids = fields.One2many('thefinalrubrica.vehicles', 'customers_id', string="Vehicles")
