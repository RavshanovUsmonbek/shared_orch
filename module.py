#!/usr/bin/python3
# coding=utf-8

#   Copyright 2021 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" Module """
from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import module
from plugins.shared_orch.utils import init_app_objects


class Module(module.ModuleModel):
    """ Pylon module """

    def __init__(self, context, descriptor):
        self.context = context
        self.descriptor = descriptor

    def init(self):
        """ Init module """
        log.info("Initializing module")

        # Init Blueprint
        self.descriptor.init_blueprint()

        # initializing db, ma
        init_app_objects(self.context.app)

        from .app_objects import db, ma
        self.descriptor.register_tool('db_orch', db)
        self.descriptor.register_tool('ma', ma)


    def deinit(self):  # pylint: disable=R0201
        """ De-init module """
        log.info("De-initializing module")
