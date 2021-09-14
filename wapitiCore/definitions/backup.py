#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of the Wapiti project (https://wapiti.sourceforge.io)
# Copyright (C) 2021 Nicolas Surribas
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
from wapitiCore.language.language import _

TYPE = "vulnerability"

NAME = _("Backup file")
SHORT_NAME = NAME

DESCRIPTION = _(
    "It may be possible to find backup files of scripts on the webserver that the web-admin put here "
    "to save a previous version or backup files that are automatically generated by the software editor used "
    "(like for example Emacs)."
) + " " + _(
    "These copies may reveal interesting information like source code or credentials."
)

SOLUTION = _(
    "The webadmin must manually delete the backup files or remove it from the web root."
) + " " + _(
    "He should also reconfigure its editor to deactivate automatic backups."
)

REFERENCES = [
    {
        "title": "OWASP: Review Old Backup and Unreferenced Files for Sensitive Information",
        "url": (
            "https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/"
            "02-Configuration_and_Deployment_Management_Testing/"
            "04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information.html"
        )
    },
    {
        "title": "CWE-530: Exposure of Backup File to an Unauthorized Control Sphere",
        "url": "https://cwe.mitre.org/data/definitions/530.html"
    },
]
