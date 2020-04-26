class FilterModule:
  @staticmethod
  def add_default_fencing(cluster, hosts_in_cluster):
    if 'fencing'              in cluster: return cluster
    if 'fencing_defaults' not in cluster: return { **cluster, 'fencing': [] }

    return { **cluster, 'fencing': [{ 'host': host } for host in hosts_in_cluster] }

  def filters(self):
    return { 'add_default_fencing': self.add_default_fencing }
