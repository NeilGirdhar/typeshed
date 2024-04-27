from _typeshed import Incomplete

from .resource import Collection, Model

class Network(Model):
    @property
    def name(self): ...
    @property
    def containers(self): ...
    def connect(self, container, *args, **kwargs): ...
    def disconnect(self, container, *args, **kwargs): ...
    def remove(self): ...

class NetworkCollection(Collection):
    model: type[Network]
    def create(self, name, *args, **kwargs): ...
    def get(self, network_id, *args, **kwargs): ...
    def list(self, *args, **kwargs): ...
    def prune(self, filters: Incomplete | None = None): ...