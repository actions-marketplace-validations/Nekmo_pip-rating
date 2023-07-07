from functools import cached_property
from typing import TYPE_CHECKING, Iterator, Set

from anytree import Node

from requirements_rating.rating import PackageRating
from requirements_rating.sources.sourcerank import SourceRank

if TYPE_CHECKING:
    from requirements_rating.dependencies import Dependencies


class Package:
    nodes: Set[Node]

    def __init__(self, requirements: "Dependencies", name: str):
        self.name = name
        self.requirements = requirements
        self.nodes = set()

    @cached_property
    def first_node(self) -> Node:
        return next(iter(self.nodes))

    @cached_property
    def sourcerank(self) -> SourceRank:
        return SourceRank(self.name)

    @cached_property
    def rating(self) -> "PackageRating":
        return PackageRating(self)

    def get_descendant_packages(self) -> Iterator["Package"]:
        for descendant in self.first_node.descendants:
            yield self.requirements.add_node_package(descendant)

    def get_child_packages(self) -> Iterator["Package"]:
        for child in self.first_node.children:
            yield self.requirements.add_node_package(child)

    def add_node(self, node: Node):
        self.nodes.add(node)

    def __repr__(self) -> str:
        return f"<Package {self.name}>"