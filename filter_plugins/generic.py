from ansible.plugins.filter.ipaddr import ipaddr

class FilterModule:
  @staticmethod
  def bool_to_str(bool_val, yes_str = 'yes', no_str = 'no'):
    return yes_str if bool_val else no_str

  @staticmethod
  def iface_to_subnet_cidr(iface):
    return ipaddr(f"{iface['ipv4']['network']}/{iface['ipv4']['netmask']}", 'net')

  def filters(self):
    return {'bool_to_str':          self.bool_to_str,
            'iface_to_subnet_cidr': self.iface_to_subnet_cidr}
    return { 'bool_to_str': bool_to_str }
