from ansible.plugins.filter.ipaddr import ipaddr

class FilterModule:
  @staticmethod
  def nth(array, index):
    return array[index - 1]

  @staticmethod
  def split(string, *args, **kwargs):
    return string.split(*args, **kwargs)

  @staticmethod
  def range_filter(size, start = 0, step = 1):
    return list(range(start, start + size, step))

  @staticmethod
  def bool_to_str(bool_val, yes_str = 'yes', no_str = 'no'):
    return yes_str if bool_val else no_str

  @staticmethod
  def to_dict_with(val, key, **kwargs):
    return { **kwargs, key: val }

  @staticmethod
  def prepend_if_not_empty(string, prefix):
    return prefix + string if string else string

  @staticmethod
  def iface_to_subnet_cidr(iface):
    return ipaddr(f"{iface['ipv4']['network']}/{iface['ipv4']['netmask']}", 'net')

  def filters(self):
    return {
      'nth':                  self.nth,
      'split':                self.split,
      'range':                self.range_filter,
      'bool_to_str':          self.bool_to_str,
      'to_dict_with':         self.to_dict_with,
      'prepend_if_not_empty': self.prepend_if_not_empty,
      'iface_to_subnet_cidr': self.iface_to_subnet_cidr
    }
