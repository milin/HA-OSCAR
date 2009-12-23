#! /usr/bin/env python
#
# Copyright (c) 2009 Himanshu Chhetri <himanshuchhetri@gmail.com>        
#                    All rights reserved.
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
 
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#   Unit tests for DatabaseDriver in CHAIF

import DatabaseDriver
from os import path
import unittest

class TestSequenceFunctions(unittest.TestCase):

  def setUp(self):
    self.db_path = "/tmp/db"
    self.schema_path = "/tmp/schema.sql"
    self.db = DatabaseDriver.DbDriver(self.db_path, self.schema_path)

  # Test Database was created successfully
  def test_create_database(self):
    self.db.create_database()
    self.assert_(path.exists(self.db_path))

if __name__ == '__main__':
  unittest.main()