class FilterModule:
  @staticmethod
  def full_name(name, resources):
    resource = next(filter(lambda res: res['name'] == name, resources), {})

    return name + '-clone' if resource.get('promotable', False) else name

  @staticmethod
  def add_default_fencing(cluster, hosts_in_cluster):
    if isinstance(cluster.get('fencing'), list): return cluster
    if not cluster.get('fencing', False): return { **cluster, 'fencing': [] }

    # cluster['fencing'] is present, non-list and truthy
    return { **cluster, 'fencing': [{ 'host': host } for host in hosts_in_cluster] }

  def filters(self):
    return {
      'full_name':           self.full_name,
      'add_default_fencing': self.add_default_fencing
    }
