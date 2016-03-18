import optparse
import os

parser = optparse.OptionParser(usage="Usage\n -d: Directory to start project\n -n Name of project")
parser.add_option("-d", action="store", dest="directory")
parser.add_option("-n", action="store", dest="name")

options, remainder = parser.parse_args()

settings_template = """

TZ = "UTC"

URLS = []

"""

try:
    os.mkdir(os.path.join(options.directory, options.name))
except Exception as e:
    print "Error while creating project: " + str(e)


