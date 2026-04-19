from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4, icmp

log = core.getLogger()


class PacketDropSimulator(object):

    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):

        packet = event.parsed
        ip_packet = packet.find('ipv4')

        if ip_packet:

            src = ip_packet.srcip
            dst = ip_packet.dstip

            log.info("Packet: %s -> %s", src, dst)

            # DROP rule 1
            if str(src) == "10.0.0.3":
                log.info("Dropping packet from h3")
                return

            # DROP rule 2
            if (str(src) == "10.0.0.1" and
                    str(dst) == "10.0.0.4"):

                if ip_packet.protocol == ipv4.ICMP_PROTOCOL:
                    log.info("Dropping ICMP from h1 to h4")
                    return

        msg = of.ofp_packet_out()
        msg.data = event.ofp

        msg.actions.append(
            of.ofp_action_output(port=of.OFPP_FLOOD)
        )

        self.connection.send(msg)


def launch():

    def start_switch(event):
        PacketDropSimulator(event.connection)

    core.openflow.addListenerByName(
        "ConnectionUp",
        start_switch
    )
