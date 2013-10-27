import socket
import ssl as libssl
import subprocess
import os
import pytz
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from MegWorld.models import ServerStatus

class Command(BaseCommand):
    args = "<server addr, server addr, ...>"
    help = "Checks server status of all or one specific server"

    def handle(self, *args, **kwargs):
        if len(args) <= 0:
            # All servers
            servers = ServerStatus.objects.all()
        else:
            # specific server(s)
            servers = []
            for arg in args:
                try:
                    servers.append(ServerStatus.objects.get(address=arg))
                except ServerStatus.DoesNotExist:
                    raise CommandError("Server address {0!r} is not found".format(arg))

        # Do server analysis
        for server in servers:
            server.online = self._is_online(server)
            server.ipv6 = self._is_online(server, ipv6=True)
            server.ssl = self._is_online(server, ssl=True, port=9000)
            server.location = self._get_location(server) 
            server.modified = datetime.now(pytz.utc)
            server.save()

    def _is_online(self, server, port=6667, ipv6=False, ssl=False):
        """ Checks if a server is online """
        if isinstance(server, ServerStatus):
            server = server.address

        if ipv6:
            test_connection = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        else:
            test_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if ssl:
            test_connection = libssl.wrap_socket(test_connection)

        try:
            test_connection.connect((server, port))
        except Exception:
            return False

        return True

    def _get_location(self, server):
        """ Gets the server location using the `geoiplookup` command """
        if isinstance(server, ServerStatus):
            server = server.address

        if os.path.isfile("GeoLiteCity.dat"):
            # we have the city database
            command = "geoiplookup -f GeoLiteCity.dat {0}".format(server)
            city = True
        else:
            # by default the datbase is usally cityless
            command = "geoiplookup {0}".format(server)
            city = False

        exe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # wait and check return code
        if exe.wait() != 0:
            return "(unknown)"
        
        stdout = exe.communicate()[0]
        
        if city:
            # Output looks like: GeoIP City Edition, Rev 1: US, MO, Kansas City, 64106, 39.106800, -94.566002, 616, 816
            stdout = stdout.split(":", 1)[-1]
            stdout = stdout.split(",")

            country = stdout[0].strip(" ")
            city = stdout[2].split(" ")
            return (city, country)
        else:
            # looks like: GeoIP Country Edition: GB, United Kingdom
            return stdout.split(":")[-1].split(",")[-1] # United Kingdom
