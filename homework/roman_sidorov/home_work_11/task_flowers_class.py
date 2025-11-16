from typing import Optional


class Flowers:

    def __init__(self, types, price, stem_length, lifetime, freshness):
        self.types = types
        self.price = price
        self.stem_length = stem_length
        self.lifetime = lifetime
        self.freshness = freshness

    def __str__(self):
        return (f"{self.types}(стойкость - {self.lifetime}дн, свежесть - {self.freshness}дн, "
                f"длина стебля - {self.stem_length}см, цена - {self.price}₽)")


class Rose(Flowers):

    def __init__(self, types, price, stem_length, lifetime, freshness):
        super().__init__(types, price, stem_length, lifetime, freshness)


class Tulip(Flowers):

    def __init__(self, types, price, stem_length, lifetime, freshness):
        super().__init__(types, price, stem_length, lifetime, freshness)


class SunFlower(Flowers):

    def __init__(self, types, price, stem_length, lifetime, freshness):
        super().__init__(types, price, stem_length, lifetime, freshness)


class Bouquet:

    def __init__(self, flowers: list[Flowers] = None):
        self.flowers: list[Flowers] = flowers or []

    def add_flower(self, flower: Flowers):
        self.flowers.append(flower)

    def add_flowers(self, *flowers: Flowers):
        self.flowers.extend(flowers)

    @property
    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    @property
    def average_freshness(self):
        if not self.flowers:
            return 0
        return sum(f.freshness for f in self.flowers) / len(self.flowers)

    def sort_by_freshness(self, reverse=False):
        self.flowers.sort(key=lambda f: f.freshness, reverse=reverse)

    def sort_by_flower(self, reverse=False):
        self.flowers.sort(key=lambda f: f.types, reverse=reverse)

    def sort_by_stem_length(self, reverse=False):
        self.flowers.sort(key=lambda f: f.stem_length, reverse=reverse)

    def sort_by_price(self, reverse=False):
        self.flowers.sort(key=lambda f: f.price, reverse=reverse)

    def __str__(self):
        text = [
            f"  Букет ({len(self.flowers)} цветка), стоимость: {self.total_price}₽, "
            f"средняя свежесть: {self.average_freshness: .1f}дн"]
        for i, f in enumerate(self.flowers, 1):
            text.append(f"  {i}. {f}")
        return "\n".join(text)

    def find_by_lifetime(self, min_day: Optional[int] = None, max_day: Optional[int] = None):
        if max_day is None:
            return [f for f in self.flowers if f.lifetime >= min_day]
        elif min_day is None:
            return [f for f in self.flowers if f.lifetime <= max_day]
        return [f for f in self.flowers if min_day <= f.lifetime <= max_day]


sun_flowers = SunFlower('Подсолнух полевой', 400, 45, 30, 15)
tulip = Tulip('Тюльпан голандский', 300, 40, 7, 2)
rose = Rose('Роза кустовая', 250, 60, 5, 3)


bouquet = Bouquet()
bouquet.add_flowers(tulip, rose, sun_flowers)
print(bouquet)

bouquet.sort_by_stem_length()
print(bouquet)

lifetime_flowers = bouquet.find_by_lifetime(6, 30)
for b in lifetime_flowers:
    print(" -", b)
