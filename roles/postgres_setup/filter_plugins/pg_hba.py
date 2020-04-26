defaults = { 'type': 'host', 'database': 'all', 'user': 'all', 'auth_method': 'md5' }

def hba(**values):
  return { **defaults, **values }

def ipv4_to_hba(ipv4, **kwargs):
  return hba(ip_address = ipv4['address'], ip_mask = ipv4['netmask'], **kwargs)

base_hba_entries = [
  hba(type = 'local', user = 'postgres', auth_method = 'peer'),
  hba(type = 'local'),
  hba(address = '127.0.0.1/32'),
  hba(address = '::1/128')
]

base_replication_hba_entries = [
  hba(type = 'local',           database = 'replication'),
  hba(address = '127.0.0.1/32', database = 'replication'),
  hba(address = '::1/128',      database = 'replication')
]

def add_base_hba_entries(hba_list):
  return base_hba_entries + hba_list

def add_base_replication_hba_entries(hba_list):
  return base_replication_hba_entries + hba_list

class FilterModule:
  def filters(self):
    return {
      'ipv4_to_hba':                      ipv4_to_hba,
      'add_base_hba_entries':             add_base_hba_entries,
      'add_base_replication_hba_entries': add_base_replication_hba_entries
    }
