from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class MulticastHelloer(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write(b'Hello World', ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print("Ack received %s from %s" % (repr(datagram), repr(address)))
        reactor.stop()

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")
        
reactor.listenMulticast(8005, MulticastHelloer(), listenMultiple=True)
reactor.run()

"""
Reference:
    https://twistedmatrix.com/documents/15.1.0/core/howto/udp.html
    https://twisted.readthedocs.io/en/twisted-17.9.0/index.html
"""