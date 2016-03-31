from __future__ import absolute_import
import optparse
import os

parser = optparse.OptionParser(usage=u"Usage\n -d: Directory to start project\n -n Name of project")
parser.add_option(u"-d", action=u"store", dest=u"directory")
parser.add_option(u"-n", action=u"store", dest=u"name")

options, remainder = parser.parse_args()

settings_template = u"""

TZ = "UTC"

URLS = []

"""

try:
    os.mkdir(os.path.join(options.directory, options.name))
except Exception, e:
    print (u"Error while creating project: " + unicode(e))


