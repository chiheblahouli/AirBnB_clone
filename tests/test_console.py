#!/usr/bin/python3
'''Contains unit tests for the AirBnB console'''
import unittest
from models import *
import sys
from io import StringIO
from unittest.mock import patch
HBNBCommand = __import__('console').HBNBCommand


class test_console(unittest.TestCase):
    '''Tests for the console'''
    def test_compile(self):
        '''
        Sends no commands, just tests to make sure it compiles without error
        '''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue().strip(), "")

    def test_help(self):
        '''Tests the help command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            out = f.getvalue().strip()
            self.assertTrue('undocumented' not in out)
            self.assertTrue('EOF' in out)
            self.assertTrue('quit' in out)
            self.assertTrue('create' in out)
            self.assertTrue('show' in out)
            self.assertTrue('destroy' in out)
            self.assertTrue('all' in out)
            self.assertTrue('update' in out)

    def test_create(self):
        '''Tests the creation of an object'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            u_id = f.getvalue().strip()
            self.assertTrue(u_id is not "")
            with open('file.json') as g:
                import json
                dic = json.loads(g.read())
                self.assertTrue("User.{}".format(u_id) in dic)
                f.close()

    def test_destroy(self):
        '''Tests the destroy console command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            u_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy User {}".format(u_id))
            with open('file.json') as g:
                import json
                dic = json.loads(g.read())
                self.assertTrue("User.{}".format(u_id) not in dic)
                f.close()

    def test_wrong_create(self):
        '''Tests create command with args wrong'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Missing class name
            HBNBCommand().onecmd("create")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class name missing **")
            f.truncate(0)
            f.seek(0)

            # Class name doesn't exist
            HBNBCommand().onecmd("create MyModel")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class doesn't exist **")
            f.truncate(0)
            f.seek(0)

    def test_wrong_show(self):
        '''Tests show command with args incorrect'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Missing class name
            HBNBCommand().onecmd("show")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class name missing **")
            f.truncate(0)
            f.seek(0)

            # Class name doesn't exist
            HBNBCommand().onecmd("show MyModel")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class doesn't exist **")
            f.truncate(0)
            f.seek(0)

            # id missing
            HBNBCommand().onecmd("show BaseModel")
            val = f.getvalue().strip()
            self.assertEqual(val, "** instance id missing **")
            f.truncate(0)
            f.seek(0)

            # id doesn't exist
            HBNBCommand().onecmd("show User 600")
            val = f.getvalue().strip()
            self.assertEqual(val, "** no instance found **")
            f.truncate(0)
            f.seek(0)

    def test_wrong_destroy(self):
        '''Tests destroy command with args incorrect'''
        with patch('sys.stdout', new=StringIO()) as f:
            # missing class
            HBNBCommand().onecmd("destroy")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class name missing **")
            f.truncate(0)
            f.seek(0)

            # Class doesnt exist
            HBNBCommand().onecmd("destroy MyModel")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class doesn't exist **")
            f.truncate(0)
            f.seek(0)

            # id missing
            HBNBCommand().onecmd("destroy User")
            val = f.getvalue().strip()
            self.assertEqual(val, "** instance id missing **")
            f.truncate(0)
            f.seek(0)

            # is doesnt exist
            HBNBCommand().onecmd("destroy User 369")
            val = f.getvalue().strip()
            self.assertEqual(val, "** no instance found **")

    def test_wrong_all(self):
        '''Tests the all command with incorrect args'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Class doesnt exist
            HBNBCommand().onecmd("all MyModel")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class doesn't exist **")

    def test_wrong_update(self):
        '''Tests the update command with incorrect args'''
        with patch('sys.stdout', new=StringIO()) as f:
            # Class missing
            HBNBCommand().onecmd("update")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class name missing **")
            f.truncate(0)
            f.seek(0)

            # Class doesnt exist
            HBNBCommand().onecmd("update fakeclass")
            val = f.getvalue().strip()
            self.assertEqual(val, "** class doesn't exist **")
            f.truncate(0)
            f.seek(0)

            # id missing
            HBNBCommand().onecmd("update Amenity")
            val = f.getvalue().strip()
            self.assertEqual(val, "** instance id missing **")
            f.truncate(0)
            f.seek(0)

            # no instance
            HBNBCommand().onecmd("update User 2468")
            val = f.getvalue().strip()
            self.assertEqual(val, "** no instance found **")
            f.truncate(0)
            f.seek(0)

            # missing attribute
            b = base_model.BaseModel()
            cm = "update BaseModel {}".format(b.id)
            HBNBCommand().onecmd(cm)
            val = f.getvalue().strip()
            self.assertEqual(val, "** attribute name missing **")
            f.truncate(0)
            f.seek(0)

            # value missing
            cm = "update BaseModel {} first_name".format(b.id)
            HBNBCommand().onecmd(cm)
            val = f.getvalue().strip()
            self.assertEqual(val, "** value missing **")
            f.truncate(0)
            f.seek(0)
