"""
新的 dataclasses 模块让你在编写你自己的类时更加方便，
如 .__init__()， .__repr__()， 和 .__eq__() 会被自动添加
"""

from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Country:
    name: str
    population: int
    area: float = field(repr=False, compare=False)
    coastline: float = 0

    def beach_per_person(self):
        """每人平均海岸线长度"""
        return (self.coastline * 1000) / self.population


def main() -> None:
    norway = Country("Norway", 5320045, 323802, 58133)
    print(norway.beach_per_person())


if __name__ == '__main__':
    main()
