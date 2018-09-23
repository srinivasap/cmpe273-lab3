from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echoer(DatagramProtocol):

    def datagramReceived(self, data, address):
        print("Data %s received from %s" % (repr(data), repr(address)))
        self.transport.write(data, address)

reactor.listenUDP(8225, Echoer())
reactor.run()

"""
Reference :
    https://twistedmatrix.com/documents/15.1.0/core/howto/udp.html
    https://twisted.readthedocs.io/en/twisted-17.9.0/index.html
"""