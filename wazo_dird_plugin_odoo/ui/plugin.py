# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import render_template

from wazo_ui.plugins.dird_source.plugin import dird_source as bp

class OdooUi(object):

    def load(self, dependencies):

        @bp.route('dird_sources/new/odoo', methods=['GET'])
        def odoo_create():
            return render_template('odoo.html')
